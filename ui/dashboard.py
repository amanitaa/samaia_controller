from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QGroupBox, QFormLayout
from PyQt5.QtCore import QTimer
import sys

from network.udp_client import receive_event


class TelemetryDashboard(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Samaya Realtime Telemetry")
        self.resize(450, 300)

        main_layout = QVBoxLayout()

        # --- ESP32 Section ---
        esp32_group = QGroupBox("ESP32 System Info")
        esp32_layout = QFormLayout()

        self.uptime_label = QLabel("--")
        self.ip_label = QLabel("--")
        self.mem_free_label = QLabel("--")
        self.mem_alloc_label = QLabel("--")
        self.cpu_freq_label = QLabel("--")
        self.cpu_temp_label = QLabel("--")

        esp32_layout.addRow("Uptime (ms):", self.uptime_label)
        esp32_layout.addRow("IP Address:", self.ip_label)
        esp32_layout.addRow("Free Memory:", self.mem_free_label)
        esp32_layout.addRow("Allocated Memory:", self.mem_alloc_label)
        esp32_layout.addRow("CPU Freq (MHz):", self.cpu_freq_label)
        esp32_layout.addRow("CPU Temp (°C):", self.cpu_temp_label)

        esp32_group.setLayout(esp32_layout)
        main_layout.addWidget(esp32_group)

        # --- Motor Section ---
        motor_group = QGroupBox("Motor Status")
        motor_layout = QFormLayout()

        self.motor_temp_label = QLabel("--")
        self.motor_load_label = QLabel("--")

        motor_layout.addRow("Motor Temp (°C):", self.motor_temp_label)
        motor_layout.addRow("Motor Load (%):", self.motor_load_label)

        motor_group.setLayout(motor_layout)
        main_layout.addWidget(motor_group)

        self.setLayout(main_layout)

        # Update loop
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_data)
        self.timer.start(250)

    def update_data(self):
        try:
            payload = receive_event()

            esp = payload["esp32"]
            motor = payload["motor"]

            self.uptime_label.setText(f"{esp['uptime_ms']}")
            self.ip_label.setText(f"{esp['ip']}")
            self.mem_free_label.setText(f"{esp['free_memory']} bytes")
            self.mem_alloc_label.setText(f"{esp['allocated_memory']} bytes")
            self.cpu_freq_label.setText(f"{esp['current_cpu_freq']} MHz")
            self.cpu_temp_label.setText(f"{esp['current_cpu_temp']} °C")

            self.motor_temp_label.setText(f"{motor['motor_temp']} °C")
            self.motor_load_label.setText(f"{motor['motor_load'] * 100:.1f} %")

        except BlockingIOError:
            pass
        except Exception as e:
            self.uptime_label.setText(f"Error: {str(e)}")


def run_gui():
    app = QApplication(sys.argv)
    win = TelemetryDashboard()
    win.show()
    sys.exit(app.exec_())
