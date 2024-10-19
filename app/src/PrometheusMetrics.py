from prometheus_client import Gauge, Info, CollectorRegistry
from src.GreenCell.UPSModel import UPSStatus
from src.Observability import *

tracer = trace.get_tracer(__name__)

identity_labels = ["ip"]

exporter_registry = CollectorRegistry()


class PrometheusMetrics:
    input_voltage = Gauge(
        "ups_input_voltage",
        "Input Voltage",
        identity_labels,
        registry=exporter_registry,
    )
    input_voltage_fault = Gauge(
        "ups_input_voltage_fault",
        "Input Voltage Fault",
        identity_labels,
        registry=exporter_registry,
    )
    output_voltage = Gauge(
        "ups_output_voltage",
        "Output Voltage",
        identity_labels,
        registry=exporter_registry,
    )
    load = Gauge("ups_load", "Load", identity_labels, registry=exporter_registry)
    input_frequency = Gauge(
        "ups_input_frequency",
        "Input Frequency",
        identity_labels,
        registry=exporter_registry,
    )
    battery_voltage = Gauge(
        "ups_battery_voltage",
        "Battery Voltage",
        identity_labels,
        registry=exporter_registry,
    )
    temperature = Gauge(
        "ups_temperature", "Temperature", identity_labels, registry=exporter_registry
    )
    utility_fail = Info(
        "ups_utility_fail", "Utility Fail", identity_labels, registry=exporter_registry
    )
    battery_low = Info(
        "ups_battery_low", "Battery Low", identity_labels, registry=exporter_registry
    )
    bypass_boost = Info(
        "ups_bypass_boost", "Bypass Boost", identity_labels, registry=exporter_registry
    )
    failed = Info("ups_failed", "Failed", identity_labels, registry=exporter_registry)
    offline = Info(
        "ups_offline", "Offline", identity_labels, registry=exporter_registry
    )
    test_in_progress = Info(
        "ups_test_in_progress",
        "Test In Progress",
        identity_labels,
        registry=exporter_registry,
    )
    shutdown_active = Info(
        "ups_shutdown_active",
        "Shutdown Active",
        identity_labels,
        registry=exporter_registry,
    )
    beeper_on = Info(
        "ups_beeper_on", "Beeper On", identity_labels, registry=exporter_registry
    )
    battery_level = Gauge(
        "ups_battery_level",
        "Battery charge level",
        identity_labels,
        registry=exporter_registry,
    )
    active = Info("ups_active", "Active", identity_labels, registry=exporter_registry)
    connected = Info(
        "ups_connected", "Connected", identity_labels, registry=exporter_registry
    )
    status = Gauge("ups_status", "Status", identity_labels, registry=exporter_registry)
    errno = Gauge("ups_errno", "Errno", identity_labels, registry=exporter_registry)
    input_voltage_nominal = Gauge(
        "ups_input_voltage_nominal",
        "Input Voltage Nominal",
        identity_labels,
        registry=exporter_registry,
    )
    input_frequency_nominal = Gauge(
        "ups_input_frequency_nominal",
        "Input Frequency Nominal",
        identity_labels,
        registry=exporter_registry,
    )
    battery_voltage_nominal = Gauge(
        "ups_battery_voltage_nominal",
        "Battery Voltage Nominal",
        identity_labels,
        registry=exporter_registry,
    )
    input_current_nominal = Gauge(
        "ups_input_current_nominal",
        "Input Current Nominal",
        identity_labels,
        registry=exporter_registry,
    )
    battery_number_nominal = Gauge(
        "ups_battery_number_nominal",
        "Battery Number Nominal",
        identity_labels,
        registry=exporter_registry,
    )
    battery_voltage_high_nominal = Gauge(
        "ups_battery_voltage_high_nominal",
        "Battery Voltage High Nominal",
        identity_labels,
        registry=exporter_registry,
    )
    battery_voltage_low_nominal = Gauge(
        "ups_battery_voltage_low_nominal",
        "Battery Voltage Low Nominal",
        identity_labels,
        registry=exporter_registry,
    )
    reg = Gauge("ups_reg", "Reg", identity_labels, registry=exporter_registry)

    @staticmethod
    @tracer.start_as_current_span("update_metrics")
    def update_metrics(ups_status: UPSStatus):
        labels = {"ip": ups_status.ip}
        PrometheusMetrics.input_voltage.labels(**labels).set(ups_status.InputVoltage)
        PrometheusMetrics.input_voltage_fault.labels(**labels).set(
            ups_status.InputVoltageFault
        )
        PrometheusMetrics.output_voltage.labels(**labels).set(ups_status.OutputVoltage)
        PrometheusMetrics.load.labels(**labels).set(ups_status.Load)
        PrometheusMetrics.input_frequency.labels(**labels).set(
            ups_status.InputFrequency
        )
        PrometheusMetrics.battery_voltage.labels(**labels).set(
            ups_status.BatteryVoltage
        )
        PrometheusMetrics.utility_fail.labels(**labels).info(
            {"UtilityFail": str(ups_status.UtilityFail)}
        )
        PrometheusMetrics.battery_low.labels(**labels).info(
            {"BatteryLow": str(ups_status.BatteryLow)}
        )
        PrometheusMetrics.bypass_boost.labels(**labels).info(
            {"BypassBoost": str(ups_status.BypassBoost)}
        )
        PrometheusMetrics.failed.labels(**labels).info(
            {"Failed": str(ups_status.Failed)}
        )
        PrometheusMetrics.offline.labels(**labels).info(
            {"Offline": str(ups_status.Offline)}
        )
        PrometheusMetrics.test_in_progress.labels(**labels).info(
            {"TestInProgress": str(ups_status.TestInProgress)}
        )
        PrometheusMetrics.shutdown_active.labels(**labels).info(
            {"ShutdownActive": str(ups_status.ShutdownActive)}
        )
        PrometheusMetrics.beeper_on.labels(**labels).info(
            {"BeeperOn": str(ups_status.BeeperOn)}
        )
        PrometheusMetrics.battery_level.labels(**labels).set(ups_status.BatteryLevel)
        PrometheusMetrics.active.labels(**labels).info(
            {"Active": str(ups_status.Active)}
        )
        PrometheusMetrics.connected.labels(**labels).info(
            {"Connected": str(ups_status.Connected)}
        )
        PrometheusMetrics.status.labels(**labels).set(ups_status.Status)
        PrometheusMetrics.errno.labels(**labels).set(ups_status.Errno)
        PrometheusMetrics.input_voltage_nominal.labels(**labels).set(
            ups_status.InputVoltageNominal
        )
        PrometheusMetrics.input_frequency_nominal.labels(**labels).set(
            ups_status.InputFrequencyNominal
        )
        PrometheusMetrics.battery_voltage_nominal.labels(**labels).set(
            ups_status.BatteryVoltageNominal
        )
        PrometheusMetrics.input_current_nominal.labels(**labels).set(
            ups_status.InputCurrentNominal
        )
        PrometheusMetrics.battery_number_nominal.labels(**labels).set(
            ups_status.BatteryNumberNominal
        )
        PrometheusMetrics.battery_voltage_high_nominal.labels(**labels).set(
            ups_status.BatteryVoltageHighNominal
        )
        PrometheusMetrics.battery_voltage_low_nominal.labels(**labels).set(
            ups_status.BatteryVoltageLowNominal
        )
        PrometheusMetrics.reg.labels(**labels).set(ups_status.Reg)

        if ups_status.Temperature is not None and ups_status.Temperature >= 0:
            PrometheusMetrics.temperature.set(ups_status.Temperature)
