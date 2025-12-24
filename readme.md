# 🦾 IoT-Based Robotic Arm Sorting System


https://github.com/user-attachments/assets/bf0d83b5-6522-493c-a97c-d7caf1e9e134


## 📘 Project Overview

This repository contains the implementation of an **IoT-based automated sorting system** developed as part of the **Advanced Embedded Systems Lab** for the **Electronic Engineering program**.

The project was developed collaboratively by **Team A** and demonstrates how **distributed embedded systems** communicate wirelessly to control a **robotic arm and conveyor belt** for **color-based object sorting** in an industrial-like scenario.

---

## 🎓 Course Context

- **Course:** Advanced Embedded Systems Lab  
- **Program:** Electronic Engineering  
- **Term:** Summer Term 2024  
- **Project Type:** University Team Project  

---

## 👥 Team Members

- Andrew Antwan  
- **David Gonzalez**  
- Shahzaib Waseem  

---

## 🎯 Target Application

The goal of this project is to simulate an **automated industrial sorting system** for small colored cubes.

The cubes are transported on a conveyor belt. When a cube reaches a predefined position, it is detected by a distance sensor. A robotic arm then picks up the cube, analyzes its color using a color sensor, and decides whether to sort it into a container or return it to the conveyor belt.

This project helps students understand:
- Autonomous embedded systems
- Wireless sensor networks
- MQTT-based communication
- Industrial automation concepts

---

## 🧠 System Architecture

### Main Components

The system is composed of four distributed components:

- Conveyor Belt  
- Distance Sensor (Ultrasonic)  
- Robotic Arm  
- Color Sensor  

Each component runs on its own embedded controller and communicates wirelessly using **MQTT over Wi-Fi**.

---

## 🔌 Hardware & Technologies

### Microcontrollers & Devices

| Device | Responsibility |
|------|----------------|
| Arduino Uno WiFi Rev2 | Distance sensor & conveyor belt control |
| Raspberry Pi Pico W | Robotic arm motors & color sensor |
| Raspberry Pi 4 | MQTT broker (central hub) |

### Communication

- **Protocol:** MQTT  
- **Broker:** Mosquitto (running on Raspberry Pi 4)  
- **Architecture:** Publish / Subscribe  

---

## 📡 MQTT Communication Model

### Publishers
- Distance Sensor → publishes object detection events  
- Color Sensor → publishes detected color  

### Subscribers
- Conveyor Belt → subscribes to stop/start commands  
- Robotic Arm → subscribes to detection and color messages  

The **robotic arm acts as both a subscriber and a publisher**, making it the central decision-making unit in the system.

---

## 🔄 System Control Flow (One Full Cycle)

The system operates in a continuous loop. One complete cycle is described below:

1. Conveyor belt runs continuously  
2. Distance sensor detects an object  
3. Distance sensor publishes a stop message  
4. Conveyor belt stops  
5. Robotic arm picks up the object  
6. Robotic arm moves the object to the color sensor  
7. Color sensor measures RGB values  
8. Detected color is published via MQTT  
9. Robotic arm decides:
   - If the object is **blue**, it is placed into the sorting container  
   - If the object is **not blue**, it is returned to the conveyor belt  
10. Robotic arm returns to its neutral position  
11. Conveyor belt resumes movement  
12. The cycle repeats  

---

## 🧩 Software Design Overview

### Distance Sensor Module
- Based on the HC-SR04 ultrasonic sensor  
- Detects objects within a configurable distance threshold  
- Publishes detection events via MQTT  

### Color Sensor Module
- Measures RGB values using frequency-based output  
- Determines dominant color via comparison logic  
- Publishes color result via MQTT  

### Motor Control Module
- Converts angles into PWM duty cycles  
- Controls robotic arm positions:
  - Pickup position  
  - Hover above color sensor  
  - Drop position  
  - Reset position  

### Conveyor Belt Module
- Controls stepper motor movement  
- Starts and stops based on MQTT messages  
- Uses direction and step pins for control  

---

## 🧪 Use Cases

### ✅ Blue Object Sorting
- Object is detected  
- Robotic arm picks it up  
- Color sensor detects blue  
- Object is placed into the sorting container  

### 🔁 Non-Blue Object Handling
- Object is detected  
- Robotic arm picks it up  
- Color sensor detects non-blue  
- Object is returned to the conveyor belt  

---

## 🛠️ System Setup & Usage

1. Place a container for blue objects at approximately 60–80° counterclockwise from the robotic arm  
2. Activate a suitable WLAN  
3. Configure SSID and password on all devices  
4. Connect the Raspberry Pi 4 (MQTT broker) to the WLAN  
5. Set the broker IP address on all sensor and actuator nodes  
6. Power all system components  
7. Place a cube on the conveyor belt  
8. Observe automatic detection, classification, and sorting  
9. The system continues operating autonomously  

---

## 📊 Diagrams (Placeholders)

Add the following diagrams to the repository for clarity:

- **Figure 1:** Sequence Diagram  
- **Figure 2:** Block Diagram  
- **Figure 3:** MQTT Communication Layout  
- **Figure 4:** Class Diagram  

---

## 📁 Project Management

- **Version Control:** GitHub  
- **Collaboration Method:**  
  - Weekly virtual planning meetings  
  - In-person hardware integration sessions  
- **Task Assignment:** Volunteer-based and skill-oriented  

---

## 📚 References

- Arduino WiFiNINA Library  
- ArduinoMqttClient Library  
- Mosquitto MQTT Broker  
- Raspberry Pi Pico W (MicroPython)  

---

## ✅ Learning Outcomes

This project demonstrates:
- Distributed embedded system design  
- MQTT-based IoT communication  
- Wireless sensor networks  
- Event-driven control logic  
- Hardware–software co-design  

---
