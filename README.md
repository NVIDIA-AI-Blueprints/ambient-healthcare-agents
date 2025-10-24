# Ambient Healthcare Agents Developer Example

**Build advanced AI agents for providers and patients using this developer example powered by NeMo Microservices, NVIDIA Nemotron, Riva ASR and TTS, and NVIDIA LLM NIM**

---
> Note: If running the NVIDIA Brev [Launchable](http://brev.nvidia.com), refer to [ambient-provider.ipynb](./ambient-provider.ipynb) and/or [ambient-patient.ipynb](./ambient-patient.ipynb) Jupyter Notebooks, which demonstrate setup and usage.
---

## Overview

Healthcare, the world's largest customer service sector, faces urgent pressure to digitize patient and provider interactions. Ambient voice AI is key, however, the next leap will come from Generative AI reasoning models—these will enable voice agents to provide intelligent, context-aware responses, automate documentation, and deliver highly personalized care, fundamentally transforming clinical workflows and scaling efficient, accurate healthcare delivery.

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
  - Parakeet 1.1b ASR Model for low-latency accurate transcription
  - Magpie Multilingual TTS Model for natural voice audio responses

- **Intelligent Guardrails**
  - NeMo Guardrails for safe and topically appropriate interactions
  - Context-aware response generation
  - Highly customizable configuration with options for guardrail-specific NIMs

---

## Software Components

### **NVIDIA Technologies**
- **llama-3.3-nemotron-super-49b-instruct** - Advanced reasoning model
- **llama-3.3-70b-instruct** - Instruction-following model for agent orchestration
- **NemoGuard Content Safety Model** - Guardrail Content safety model
- **NemoGuard Topic Control Model** - Guardrail Topic control model
- **Riva Magpie TTS** - Text-to-speech synthesis
- **Riva Parakeet ASR** - Automatic speech recognition
- **NVIDIA ace-controller** - Voice AI Service orchestration

### **Additional Software**
- **LangChain** & **Langgraph** - Framework for Agentic LLM applications

---

## System Requirements

### **Minimum Requirements**

> **Note:** Users may have to wait 5–10 minutes for the instance to start, depending on cloud availability.

#### **Operating System & System Software**
- **Ubuntu 22.04**
- **Docker Version 28.1+ with Docker Compose plugin**

#### **Storage**
- **Ambient Patient Agent:** 302 GB (for self-hosted configuration)
- **Ambient Provider Agent:** 325 GB (for self-hosted configuration)

### **Hardware Requirements**

#### **Ambient Provider Agent**

**Self-Hosted Configuration:**
| Service | Use Case | Recommended GPU |
|---------|----------|-----------------|
| [Riva ASR NIM](https://build.nvidia.com/nvidia/parakeet-ctc-1_1b-asr/modelcard) | Audio Transcription and Diarization | 1x various options including L40, A100, and more (see [modelcard](https://build.nvidia.com/nvidia/parakeet-ctc-1_1b-asr/modelcard)) |
| [Reasoning Model](https://docs.nvidia.com/nim/large-language-models/latest/supported-models.html#llama-33-nemotron-super-49b-v1) | Medical Note (SOAP) Generation | 2x H100 80 GB<br>*or* 4x A100 80 GB |

**NVIDIA API Catalog Configuration:** 
<br>No GPU requirement when using public NVIDIA endpoints for NIM microservices (build.nvidia.com)


#### **Ambient Patient Agent**

**Self-Hosted Configuration:**
| Service | Use Case | Recommended GPU |
|---------|----------|-----------------|
| [Riva ASR NIM](https://build.nvidia.com/nvidia/parakeet-ctc-1_1b-asr/modelcard) | Speech-to-Text Transcription | 1x various options including L40, A100, and more (see [modelcard](https://build.nvidia.com/nvidia/parakeet-ctc-1_1b-asr/modelcard)) |
| [Riva TTS NIM](https://build.nvidia.com/nvidia/magpie-tts-multilingual/modelcard) | Text-to-Speech Generation | 1x various options including L40, A100, and more (see [modelcard](https://build.nvidia.com/nvidia/magpie-tts-multilingual/modelcard)) |
[NemoGuard Content Safety Model](https://build.nvidia.com/nvidia/llama-3_1-nemoguard-8b-content-safety/modelcard) (Optional for Enabling NeMo Guardrails) | `nvidia/llama-3_1-nemoguard-8b-content-safety` | 1x options including A100, H100, L40S, A6000 (see [modelcard](https://build.nvidia.com/nvidia/llama-3_1-nemoguard-8b-content-safety/modelcard))
[NemoGuard Topic Control Model](https://build.nvidia.com/nvidia/llama-3_1-nemoguard-8b-topic-control/modelcard) (Optional for Enabling NeMo Guardrails) | `nvidia/llama-3_1-nemoguard-8b-topic-control` | 1x options including A100, H100, L40S, A6000 (see [modelcard](https://build.nvidia.com/nvidia/llama-3_1-nemoguard-8b-topic-control/modelcard))
| [Instruct Model](https://build.nvidia.com/meta/llama-3_3-70b-instruct/modelcard) | Agent Reasoning and Tool Calling | 2x H100 80 GB<br>*or* 4x A100 80GB (see [modelcard](https://build.nvidia.com/meta/llama-3_3-70b-instruct/modelcard)) |

**NVIDIA API Catalog Configuration:** 
<br>No GPU requirement when using public NVIDIA endpoints for NIM microservices (build.nvidia.com)

---

## Deployment Options

- **Docker Compose** - Containerized deployment
   - **NVIDIA API Catalog Endpoints** - Using NVIDIA's hosted services [build.nvidia.com](https://build.nvidia.com).
   - **Self-Hosted** - Local GPU deployment

### **Quickstart**

Ensure that the underlying repositories ```ambient-provider``` and ```ambient-patient``` are cloned.

```bash
git submodule update --init --recursive --remote
```

For a quickstart, refer to [ambient-provider](https://github.com/NVIDIA-AI-Blueprints/ambient-provider/tree/main#quick-start) and/or [ambient-patient](https://github.com/NVIDIA-AI-Blueprints/ambient-patient/tree/main#getting-started), which demonstrate setup and usage.

---

## Deploying on NVIDIA Brev

For a streamlined cloud deployment experience, you can deploy the Ambient Healthcare Agents developer example on NVIDIA Brev using a preconfigured GPU Environment Template (Launchable) [here](http://brev.nvidia.com). While this launchable allows for deploying both ambient provider and ambient patient healthcare agents, please run one notebook at a time.

### Why Choose NVIDIA Brev?

- **One-Click Deployment**: Pre-configured GPU environments with automatic setup
- **Managed Infrastructure**: No need to manage servers or GPU clusters
- **Secure Access**: Built-in secure tunneling for web interface access  
- **Flexible Resources**: Choose from H100, A100, and other GPU configurations
- **Cost-Effective**: Pay only for actual usage time

---

## Ethical Considerations

NVIDIA believes Trustworthy AI is a shared responsibility, and we have established policies and practices to enable development for a wide array of AI applications. When downloaded or used in accordance with our terms of service, developers should work with their supporting model team to ensure the models meet requirements for the relevant industry and use case and addresses unforeseen product misuse. 

For more detailed information on ethical considerations for the models, please see the Model Card++ Explainability, Bias, Safety & Security, and Privacy Subcards. 

**Report Issues:** Please report security vulnerabilities or NVIDIA AI Concerns [here](https://www.nvidia.com/en-us/support/submit-security-vulnerability/).

---

## Security Considerations

Please be aware of the following security considerations when using this repository:

- This repository and its contents is shared as a reference and is provided "as is". The security in the production environment is the responsibility of the end users deploying it. When deploying in a production environment, please have security experts review any potential risks and threats; define the trust boundaries, implement logging and monitoring capabilities, secure the communication channels, integrate AuthN & AuthZ with appropriate access controls, keep the deployment up to date, ensure the containers/source code are secure and free of known vulnerabilities.
- A frontend that handles AuthN & AuthZ should be in place as missing AuthN & AuthZ could provide ungated access to customer models if directly exposed to e.g. the internet, resulting in either cost to the customer, resource exhaustion, or denial of service.
- The repository doesn't require any privileged access to the system.
- The end users are responsible for ensuring the availability of their deployment.
- The end users are responsible for building the container images and keeping them up to date.
- The end users are responsible for ensuring that OSS packages used by the developer example are current.
- The logs from the agent backend and UI frontend containers are printed to standard out. They can include input prompts and output completions for development purposes. The end users are advised to handle logging securely and avoid information leakage for production use cases.
- The agent backend and UI frontend containers may interact with local files for development purposes. The end users are advised to customize all file saving and uploading logic securely and avoid information leakage for production use cases.
- Credential Management: Never hard-code sensitive credentials (API keys, passwords, etc.) in code or configuration files. Use environment variables or a secrets manager.
- NGC API Key: The developer examples require and process an NVIDIA NGC API key. Treat your key as sensitive; do not expose it publicly or commit it to source control.
- Network Exposure: By default, several services run locally and may expose network ports. Restrict access with firewalls or Docker network settings as appropriate for your environment.
- User Data Protection: Uploaded audio files and generated medical notes may contain personally identifiable information (PII) or protected health information (PHI). Ensure secure storage and proper data handling in accordance with applicable regulations (e.g., HIPAA, GDPR).
- Dependencies: Review all dependencies and container images for known vulnerabilities. Keep your dependencies up to date.
- Container Security: Do not run containers with unnecessary privileges. Use the least privilege principle.
- Vulnerability Reporting: If you discover any security issues or vulnerabilities in this repository, please follow the reporting instructions in the [SECURITY.md](./SECURITY.md) file.

For more information, see the [SECURITY.md](./SECURITY.md) file in this repository.


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

---