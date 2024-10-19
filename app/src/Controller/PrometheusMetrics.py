import src.GreenCell as GC
from src.PrometheusMetrics import PrometheusMetrics


class Prometheus:

    @staticmethod
    def update():
        ups_status = GC.GreenCell.get_UPS_status()
        PrometheusMetrics.update_metrics(ups_status)
