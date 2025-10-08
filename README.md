# Ambient Healthcare Agents Developer Example

**Build advanced AI agents for providers and patients using this developer example powered by NeMo Microservices, NVIDIA Nemotron, Riva ASR and TTS, and NVIDIA LLM NIM**

> ⚠️ **Third-Party Software Notice**  
> This project will download and install additional third-party open source software projects.  
> Please review the license terms of these open source projects before use.

---

## Overview

Healthcare, the world's largest customer service sector, faces urgent pressure to digitize patient interactions. Ambient voice AI is key, however, the next leap will come from Generative AI reasoning models—these will enable voice agents to provide intelligent, context-aware responses, automate documentation, and deliver highly personalized care, fundamentally transforming workflows and scaling efficient, accurate healthcare delivery.

This developer example provides developers with the ingredients to build and scale such agents with two primary use cases:

### **Ambient Provider Voice Agent**
Does more than transcribe patient-provider conversations. It understands context, infers intent, and generates nuanced, structured clinical documentation—such as SOAP notes—autonomously, reducing manual input and supporting better clinical decisions.

### **Ambient Patient Voice Agent**
Manages high-volume patient touchpoints (e.g., clinic intake, surveys, appointment scheduling, information queries) without clinician involvement. Its ability to reason dynamically allows for more personalized, empathetic patient interactions and real-time problem-solving within complex healthcare contexts.

---

## Architecture

![Architecture Diagram](assets/architecture-diagram.png)

*Figure: System architecture showing integration of NeMo Microservices, NVIDIA Nemotron, Riva ASR & TTS, and LLM NIM for provider and patient voice agents.*

---

## Key Features

### **Ambient Provider Agent**

- **Advanced Transcription**
  - Riva transcription with speaker diarization and medical terminology lexicon boosting
  - Parakeet ASR for real-time diarized transcription
  - Support for both live conversations and retrospective analysis

- **Fast Medical Reasoning**
  - Llama Nemotron reasoning capabilities deliver highest accuracy and lowest latency
  - Automated analysis of transcripts for clinical documentation
  - Autonomous SOAP note generation

### **Ambient Patient Agent**

- **Comprehensive Speech Pipeline**
  - Riva speech-to-text and text-to-speech capabilities
  - Parakeet 1.1b ASR Model for accurate transcription
  - Magpie Multilingual TTS Model for natural responses

- **Intelligent Guardrails**
  - NeMo Guardrails for safe and appropriate interactions
  - Context-aware response generation
  - Multi-language support

---

## Software Components

### **NVIDIA Technologies**
- `llama-3.3-nemotron-super-49b-instruct` - Advanced reasoning model
- `llama-3.3-70b-instruct` - Instruction-following model
- **Riva Magpie TTS** - Text-to-speech synthesis
- **Riva Parakeet ASR** - Automatic speech recognition
- **ace-controller** - Service orchestration

### **Additional Software**
- **LangChain** - Framework for LLM applications
- **Tavily** - Web search and retrieval

---

## System Requirements

### **Minimum Requirements**

> **Note:** Users may have to wait 5–10 minutes for the instance to start, depending on cloud availability.

#### **Operating System**
- Ubuntu 22.04

#### **Disk Space**
- **Ambient Patient Agent:** No additional disk space required
- **Ambient Provider Agent:** 75 GB (325 GB total if self-hosting reasoning model NIM)

### **Hardware Requirements**

#### **Ambient Provider Agent**

**Self-Hosted Configuration:**
| Service | Use Case | Recommended GPU |
|---------|----------|-----------------|
| Riva ASR Microservice | Audio Transcription and Diarization | 1 x L40 |
| Reasoning Model | Medical Note (SOAP) Generation | 2 x H100 250 GB<br>*or* 4 x A100 250 GB |

**Cloud Configuration:** No GPU requirement when using public NVIDIA endpoints (build.nvidia.com)

#### **Ambient Patient Agent**

**Self-Hosted Configuration:**
| Service | Use Case | Recommended GPU |
|---------|----------|-----------------|
| Riva ASR Microservice | Speech-to-Text Transcription | 1 x L40S |
| Riva TTS Microservice | Text-to-Speech Generation | 1 x L40S |
| Instruct Model | Agent Reasoning and Tool Calling | 2 x H100 80 GB<br>*or* 4 x A100 80GB |

**Cloud Configuration:** No GPU requirement when using public NVIDIA endpoints (build.nvidia.com)

---

## Deployment Options

- **Docker Compose** - Containerized deployment
- **Cloud Endpoints** - Using NVIDIA's hosted services
- **Self-Hosted** - Local GPU deployment

### **Quickstart**
For a quickstart, refer to the `ambient-provider` and `ambient-patient` Python notebooks, which demonstrate setup and usage.

---

## Ethical Considerations

NVIDIA believes Trustworthy AI is a shared responsibility, and we have established policies and practices to enable development for a wide array of AI applications. When downloaded or used in accordance with our terms of service, developers should work with their supporting model team to ensure the models meet requirements for the relevant industry and use case and addresses unforeseen product misuse. 

For more detailed information on ethical considerations for the models, please see the Model Card++ Explainability, Bias, Safety & Security, and Privacy Subcards. 

**Report Issues:** Please report security vulnerabilities or NVIDIA AI Concerns [here](https://www.nvidia.com/en-us/support/submit-security-vulnerability/).

---

## License and Terms of Use

### **License**
Use of the models in this developer example is governed by the **NVIDIA AI Foundation Models Community License**.

### **Governing Terms**
- **NVIDIA Ambient Healthcare Agents Developer Example:** Apache 2.0 License
- **Software and Materials:** NVIDIA Software License Agreement and Product-Specific Terms for NVIDIA AI Products
- **Models (except Llama-3.3-Nemotron-Super-49B-v1.5):** NVIDIA Community Model License
- **Llama-3.3-Nemotron-Super-49B-v1.5 Model:** NVIDIA Open Model License Agreement
- **Llama-3.3-70b-Instruct Model:** Llama 3.3 Community License Agreement

*Built with Llama.*

---