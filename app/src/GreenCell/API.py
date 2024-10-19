import datetime
import os
import requests
from functools import cache
from dotenv import load_dotenv
from src.GreenCell.UPSModel import UPSStatus
from src.Observability import *

tracer = trace.get_tracer(__name__)

load_dotenv()


class GreenCell:
    __ip: str = os.getenv("GC_APP_IP", "localhost")
    __port: str = os.getenv("GC_APP_PORT", "8080")
    __protocol: str = os.getenv("GC_APP_PROTOCOL", "http")
    __password: str = os.getenv("GC_PASSWORD", None)

    __login_path: str = "/api/login"
    __data_path: str = "/api/current_parameters"

    __access_token: str = None
    __expiration_date: datetime.datetime = None

    @staticmethod
    @tracer.start_as_current_span("get_UPS_status")
    def get_UPS_status() -> UPSStatus:
        span = get_current_span()
        span.set_attribute("UPS_ip", GreenCell.__ip)

        response = requests.get(
            url=GreenCell.__get_url(GreenCell.__data_path),
            headers={
                "Content-Type": "application/json",
                "Authorization": f"Bearer {GreenCell.__get_token()}",
            },
        )
        if response.status_code >= 300 or response.status_code < 200:
            raise Exception("Failed get UPS status from GreenCell API")

        result: dict[str, str] = response.json()

        set_current_span_status()
        return UPSStatus(
            **{
                "ip": GreenCell.__ip,
                **result,
            }
        )

    @staticmethod
    @tracer.start_as_current_span("get_token")
    def __get_token() -> str:
        if (not GreenCell.is_logged_in()) or GreenCell.__is_token_expired():
            logger.warning("GreenCell token is expired, logging in again")
            GreenCell.login()
        return GreenCell.__access_token

    @staticmethod
    @tracer.start_as_current_span("login")
    def login() -> None:
        if GreenCell.__password is None:
            raise Exception("GreenCell password is not set")

        response = requests.post(
            url=GreenCell.__get_url(GreenCell.__login_path),
            json={"password": GreenCell.__password},
            headers={"Content-Type": "application/json"},
        )
        if response.status_code >= 300 or response.status_code < 200:
            raise Exception("Failed to login to GreenCell API")

        result: dict[str, str] = response.json()
        GreenCell.__access_token = result["access_token"]
        GreenCell.__expiration_date = datetime.datetime.strptime(
            result["expiration_date"], "%Y-%m-%dT%H:%M:%S.%fZ"
        )
        logger.info("Logged in to GreenCell API successfully")

    @staticmethod
    def __is_token_expired():
        return datetime.datetime.now() > GreenCell.__expiration_date

    @staticmethod
    def is_logged_in():
        return GreenCell.__access_token is not None

    @cache
    @staticmethod
    def __get_url(path: str) -> str:
        return GreenCell.__get_base_url() + path

    @cache
    @staticmethod
    def __get_base_url() -> str:
        return "{protocol}://{ip}:{port}".format(
            protocol=GreenCell.__protocol,
            ip=GreenCell.__ip,
            port=GreenCell.__port,
        )
