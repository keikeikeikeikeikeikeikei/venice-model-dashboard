window.veniceModels = {
  "text": [
    {
      "created": 1742262554,
      "id": "venice-uncensored",
      "model_spec": {
        "pricing": {
          "input": {
            "usd": 0.2,
            "diem": 0.2
          },
          "output": {
            "usd": 0.9,
            "diem": 0.9
          }
        },
        "availableContextTokens": 32768,
        "capabilities": {
          "optimizedForCode": false,
          "quantization": "fp16",
          "supportsFunctionCalling": false,
          "supportsReasoning": false,
          "supportsResponseSchema": true,
          "supportsVision": false,
          "supportsWebSearch": true,
          "supportsLogProbs": true
        },
        "constraints": {
          "temperature": {
            "default": 0.7
          },
          "top_p": {
            "default": 0.9
          }
        },
        "name": "Venice Uncensored 1.1",
        "modelSource": "https://huggingface.co/cognitivecomputations/Dolphin-Mistral-24B-Venice-Edition",
        "offline": false,
        "traits": [
          "most_uncensored"
        ]
      },
      "object": "model",
      "owned_by": "venice.ai",
      "type": "text"
    },
    {
      "created": 1745903059,
      "id": "qwen3-4b",
      "model_spec": {
        "pricing": {
          "input": {
            "usd": 0.05,
            "diem": 0.05
          },
          "output": {
            "usd": 0.15,
            "diem": 0.15
          }
        },
        "availableContextTokens": 32768,
        "capabilities": {
          "optimizedForCode": false,
          "quantization": "fp8",
          "supportsFunctionCalling": true,
          "supportsReasoning": true,
          "supportsResponseSchema": true,
          "supportsVision": false,
          "supportsWebSearch": true,
          "supportsLogProbs": true
        },
        "constraints": {
          "temperature": {
            "default": 0.6
          },
          "top_p": {
            "default": 0.95
          }
        },
        "name": "Venice Small",
        "modelSource": "https://huggingface.co/Qwen/Qwen3-4B",
        "offline": false,
        "traits": []
      },
      "object": "model",
      "owned_by": "venice.ai",
      "type": "text"
    },
    {
      "created": 1742262554,
      "id": "mistral-31-24b",
      "model_spec": {
        "pricing": {
          "input": {
            "usd": 0.5,
            "diem": 0.5
          },
          "output": {
            "usd": 2,
            "diem": 2
          }
        },
        "availableContextTokens": 131072,
        "capabilities": {
          "optimizedForCode": false,
          "quantization": "fp8",
          "supportsFunctionCalling": true,
          "supportsReasoning": false,
          "supportsResponseSchema": true,
          "supportsVision": true,
          "supportsWebSearch": true,
          "supportsLogProbs": false
        },
        "constraints": {
          "temperature": {
            "default": 0.15
          },
          "top_p": {
            "default": 1
          }
        },
        "name": "Venice Medium",
        "modelSource": "https://huggingface.co/mistralai/Mistral-Small-3.1-24B-Instruct-2503",
        "offline": false,
        "traits": [
          "default_vision"
        ]
      },
      "object": "model",
      "owned_by": "venice.ai",
      "type": "text"
    },
    {
      "created": 1745903059,
      "id": "qwen3-235b",
      "model_spec": {
        "pricing": {
          "input": {
            "usd": 0.45,
            "diem": 0.45
          },
          "output": {
            "usd": 3.5,
            "diem": 3.5
          }
        },
        "availableContextTokens": 131072,
        "capabilities": {
          "optimizedForCode": false,
          "quantization": "fp8",
          "supportsFunctionCalling": true,
          "supportsReasoning": true,
          "supportsResponseSchema": true,
          "supportsVision": false,
          "supportsWebSearch": true,
          "supportsLogProbs": true
        },
        "constraints": {
          "temperature": {
            "default": 0.6
          },
          "top_p": {
            "default": 0.95
          }
        },
        "name": "Venice Large 1.1",
        "modelSource": "https://huggingface.co/Qwen/Qwen3-235B-A22B-Instruct-2507-FP8",
        "offline": false,
        "traits": []
      },
      "object": "model",
      "owned_by": "venice.ai",
      "type": "text"
    },
    {
      "created": 1745903059,
      "id": "qwen3-235b-a22b-thinking-2507",
      "model_spec": {
        "pricing": {
          "input": {
            "usd": 0.45,
            "diem": 0.45
          },
          "output": {
            "usd": 3.5,
            "diem": 3.5
          }
        },
        "availableContextTokens": 131072,
        "capabilities": {
          "optimizedForCode": false,
          "quantization": "fp8",
          "supportsFunctionCalling": true,
          "supportsReasoning": true,
          "supportsResponseSchema": true,
          "supportsVision": false,
          "supportsWebSearch": true,
          "supportsLogProbs": true
        },
        "constraints": {
          "temperature": {
            "default": 0.6
          },
          "top_p": {
            "default": 0.95
          }
        },
        "name": "Qwen 3 235B A22B Thinking 2507",
        "modelSource": "https://huggingface.co/Qwen/Qwen3-235B-A22B-Thinking-2507-FP8",
        "offline": false,
        "traits": []
      },
      "object": "model",
      "owned_by": "venice.ai",
      "type": "text"
    },
    {
      "created": 1745903059,
      "id": "qwen3-235b-a22b-instruct-2507",
      "model_spec": {
        "pricing": {
          "input": {
            "usd": 0.15,
            "diem": 0.15
          },
          "output": {
            "usd": 0.75,
            "diem": 0.75
          }
        },
        "availableContextTokens": 131072,
        "capabilities": {
          "optimizedForCode": false,
          "quantization": "fp8",
          "supportsFunctionCalling": true,
          "supportsReasoning": false,
          "supportsResponseSchema": true,
          "supportsVision": false,
          "supportsWebSearch": true,
          "supportsLogProbs": true
        },
        "constraints": {
          "temperature": {
            "default": 0.7
          },
          "top_p": {
            "default": 0.8
          }
        },
        "name": "Qwen 3 235B A22B Instruct 2507",
        "modelSource": "https://huggingface.co/Qwen/Qwen3-235B-A22B-Instruct-2507-FP8",
        "offline": false,
        "traits": []
      },
      "object": "model",
      "owned_by": "venice.ai",
      "type": "text"
    },
    {
      "created": 1745903059,
      "id": "qwen3-next-80b",
      "model_spec": {
        "pricing": {
          "input": {
            "usd": 0.35,
            "diem": 0.35
          },
          "output": {
            "usd": 1.9,
            "diem": 1.9
          }
        },
        "availableContextTokens": 262144,
        "capabilities": {
          "optimizedForCode": false,
          "quantization": "fp16",
          "supportsFunctionCalling": true,
          "supportsReasoning": false,
          "supportsResponseSchema": true,
          "supportsVision": false,
          "supportsWebSearch": true,
          "supportsLogProbs": true
        },
        "constraints": {
          "temperature": {
            "default": 0.7
          },
          "top_p": {
            "default": 0.8
          }
        },
        "name": "Qwen 3 Next 80b",
        "modelSource": "https://huggingface.co/Qwen/Qwen3-Next-80B-A3B-Instruct",
        "offline": false,
        "traits": []
      },
      "object": "model",
      "owned_by": "venice.ai",
      "type": "text"
    },
    {
      "created": 1745903059,
      "id": "qwen3-coder-480b-a35b-instruct",
      "model_spec": {
        "pricing": {
          "input": {
            "usd": 0.75,
            "diem": 0.75
          },
          "output": {
            "usd": 3,
            "diem": 3
          }
        },
        "availableContextTokens": 262144,
        "capabilities": {
          "optimizedForCode": false,
          "quantization": "fp8",
          "supportsFunctionCalling": true,
          "supportsReasoning": false,
          "supportsResponseSchema": true,
          "supportsVision": false,
          "supportsWebSearch": true,
          "supportsLogProbs": true
        },
        "constraints": {
          "temperature": {
            "default": 0.7
          },
          "top_p": {
            "default": 0.8
          }
        },
        "name": "Qwen 3 Coder 480b",
        "modelSource": "https://huggingface.co/Qwen/Qwen3-Coder-480B-A35B-Instruct",
        "offline": false,
        "traits": [
          "default_code"
        ]
      },
      "object": "model",
      "owned_by": "venice.ai",
      "type": "text"
    },
    {
      "created": 1711929600,
      "id": "hermes-3-llama-3.1-405b",
      "model_spec": {
        "pricing": {
          "input": {
            "usd": 1.1,
            "diem": 1.1
          },
          "output": {
            "usd": 3,
            "diem": 3
          }
        },
        "availableContextTokens": 131072,
        "capabilities": {
          "optimizedForCode": false,
          "quantization": "fp8",
          "supportsFunctionCalling": false,
          "supportsReasoning": false,
          "supportsResponseSchema": false,
          "supportsVision": false,
          "supportsWebSearch": true,
          "supportsLogProbs": false
        },
        "constraints": {
          "temperature": {
            "default": 0.7
          },
          "top_p": {
            "default": 0.9
          }
        },
        "name": "Hermes 3 Llama 3.1 405b",
        "modelSource": "https://huggingface.co/NousResearch/Hermes-3-Llama-3.1-405B",
        "offline": false,
        "traits": []
      },
      "object": "model",
      "owned_by": "venice.ai",
      "type": "text"
    },
    {
      "created": 1711929600,
      "id": "google-gemma-3-27b-it",
      "model_spec": {
        "pricing": {
          "input": {
            "usd": 0.12,
            "diem": 0.12
          },
          "output": {
            "usd": 0.2,
            "diem": 0.2
          }
        },
        "availableContextTokens": 202752,
        "capabilities": {
          "optimizedForCode": false,
          "quantization": "fp8",
          "supportsFunctionCalling": true,
          "supportsReasoning": false,
          "supportsResponseSchema": true,
          "supportsVision": true,
          "supportsWebSearch": true,
          "supportsLogProbs": false
        },
        "constraints": {
          "temperature": {
            "default": 0.7
          },
          "top_p": {
            "default": 0.9
          }
        },
        "name": "Google Gemma 3 27B Instruct",
        "modelSource": "https://huggingface.co/google/gemma-3-27b-it",
        "offline": false,
        "traits": []
      },
      "object": "model",
      "owned_by": "venice.ai",
      "type": "text"
    },
    {
      "created": 1745903059,
      "id": "grok-41-fast",
      "model_spec": {
        "pricing": {
          "input": {
            "usd": 0.5,
            "diem": 0.5
          },
          "output": {
            "usd": 1.25,
            "diem": 1.25
          }
        },
        "availableContextTokens": 262144,
        "capabilities": {
          "optimizedForCode": false,
          "quantization": "not-available",
          "supportsFunctionCalling": true,
          "supportsReasoning": true,
          "supportsResponseSchema": true,
          "supportsVision": true,
          "supportsWebSearch": true,
          "supportsLogProbs": true
        },
        "constraints": {
          "temperature": {
            "default": 0.7
          },
          "top_p": {
            "default": 0.8
          }
        },
        "name": "Grok 4.1 Fast",
        "modelSource": "",
        "offline": false,
        "traits": []
      },
      "object": "model",
      "owned_by": "venice.ai",
      "type": "text"
    },
    {
      "created": 1717795200,
      "id": "gemini-3-pro-preview",
      "model_spec": {
        "pricing": {
          "input": {
            "usd": 2.5,
            "diem": 2.5
          },
          "output": {
            "usd": 15,
            "diem": 15
          }
        },
        "availableContextTokens": 202752,
        "capabilities": {
          "optimizedForCode": false,
          "quantization": "not-available",
          "supportsFunctionCalling": true,
          "supportsReasoning": true,
          "supportsResponseSchema": true,
          "supportsVision": true,
          "supportsWebSearch": true,
          "supportsLogProbs": true
        },
        "constraints": {
          "temperature": {
            "default": 0.7
          },
          "top_p": {
            "default": 0.8
          }
        },
        "name": "Gemini 3 Pro Preview",
        "modelSource": "https://deepmind.google/models/gemini/pro/",
        "offline": false,
        "traits": []
      },
      "object": "model",
      "owned_by": "venice.ai",
      "type": "text"
    },
    {
      "created": 1765503106,
      "id": "claude-opus-45",
      "model_spec": {
        "pricing": {
          "input": {
            "usd": 6,
            "diem": 6
          },
          "output": {
            "usd": 30,
            "diem": 30
          }
        },
        "availableContextTokens": 202752,
        "capabilities": {
          "optimizedForCode": true,
          "quantization": "not-available",
          "supportsFunctionCalling": true,
          "supportsReasoning": true,
          "supportsResponseSchema": true,
          "supportsVision": true,
          "supportsWebSearch": true,
          "supportsLogProbs": false
        },
        "constraints": {
          "temperature": {
            "default": 0.7
          },
          "top_p": {
            "default": 0.9
          }
        },
        "name": "Claude Opus 4.5",
        "modelSource": "",
        "offline": false,
        "traits": []
      },
      "object": "model",
      "owned_by": "venice.ai",
      "type": "text"
    },
    {
      "created": 1711929600,
      "id": "openai-gpt-oss-120b",
      "model_spec": {
        "pricing": {
          "input": {
            "usd": 0.07,
            "diem": 0.07
          },
          "output": {
            "usd": 0.3,
            "diem": 0.3
          }
        },
        "availableContextTokens": 131072,
        "capabilities": {
          "optimizedForCode": false,
          "quantization": "not-available",
          "supportsFunctionCalling": true,
          "supportsReasoning": false,
          "supportsResponseSchema": false,
          "supportsVision": false,
          "supportsWebSearch": true,
          "supportsLogProbs": false
        },
        "constraints": {
          "temperature": {
            "default": 0.7
          },
          "top_p": {
            "default": 0.9
          }
        },
        "name": "OpenAI GPT OSS 120B",
        "modelSource": "https://huggingface.co/openai/gpt-oss-120b",
        "offline": false,
        "traits": []
      },
      "object": "model",
      "owned_by": "venice.ai",
      "type": "text"
    },
    {
      "created": 1717795200,
      "id": "kimi-k2-thinking",
      "model_spec": {
        "pricing": {
          "input": {
            "usd": 0.75,
            "diem": 0.75
          },
          "output": {
            "usd": 3.2,
            "diem": 3.2
          }
        },
        "availableContextTokens": 262144,
        "capabilities": {
          "optimizedForCode": true,
          "quantization": "int4",
          "supportsFunctionCalling": true,
          "supportsReasoning": true,
          "supportsResponseSchema": true,
          "supportsVision": false,
          "supportsWebSearch": true,
          "supportsLogProbs": true
        },
        "constraints": {
          "temperature": {
            "default": 0.7
          },
          "top_p": {
            "default": 0.8
          }
        },
        "name": "Kimi K2 Thinking",
        "modelSource": "https://huggingface.co/moonshotai/Kimi-K2-Thinking",
        "offline": false,
        "traits": []
      },
      "object": "model",
      "owned_by": "venice.ai",
      "type": "text"
    },
    {
      "created": 1711929600,
      "id": "zai-org-glm-4.6",
      "model_spec": {
        "pricing": {
          "input": {
            "usd": 0.85,
            "diem": 0.85
          },
          "output": {
            "usd": 2.75,
            "diem": 2.75
          }
        },
        "availableContextTokens": 202752,
        "capabilities": {
          "optimizedForCode": false,
          "quantization": "fp8",
          "supportsFunctionCalling": true,
          "supportsReasoning": false,
          "supportsResponseSchema": true,
          "supportsVision": false,
          "supportsWebSearch": true,
          "supportsLogProbs": false
        },
        "constraints": {
          "temperature": {
            "default": 0.7
          },
          "top_p": {
            "default": 0.9
          }
        },
        "name": "GLM 4.6",
        "modelSource": "https://huggingface.co/zai-org/GLM-4.6",
        "offline": false,
        "traits": []
      },
      "object": "model",
      "owned_by": "venice.ai",
      "type": "text"
    },
    {
      "created": 1765065600,
      "id": "deepseek-v3.2",
      "model_spec": {
        "pricing": {
          "input": {
            "usd": 0.4,
            "diem": 0.4
          },
          "output": {
            "usd": 1,
            "diem": 1
          }
        },
        "availableContextTokens": 163840,
        "capabilities": {
          "optimizedForCode": false,
          "quantization": "not-available",
          "supportsFunctionCalling": false,
          "supportsReasoning": false,
          "supportsResponseSchema": false,
          "supportsVision": false,
          "supportsWebSearch": true,
          "supportsLogProbs": false
        },
        "constraints": {
          "temperature": {
            "default": 1
          },
          "top_p": {
            "default": 0.95
          }
        },
        "name": "DeepSeek V3.2",
        "modelSource": "https://huggingface.co/deepseek-ai/DeepSeek-V3.2",
        "offline": false,
        "traits": []
      },
      "object": "model",
      "owned_by": "venice.ai",
      "type": "text"
    },
    {
      "created": 1727966436,
      "id": "llama-3.2-3b",
      "model_spec": {
        "pricing": {
          "input": {
            "usd": 0.15,
            "diem": 0.15
          },
          "output": {
            "usd": 0.6,
            "diem": 0.6
          }
        },
        "availableContextTokens": 131072,
        "capabilities": {
          "optimizedForCode": false,
          "quantization": "fp16",
          "supportsFunctionCalling": true,
          "supportsReasoning": false,
          "supportsResponseSchema": true,
          "supportsVision": false,
          "supportsWebSearch": true,
          "supportsLogProbs": true
        },
        "constraints": {
          "temperature": {
            "default": 0.6
          },
          "top_p": {
            "default": 0.95
          }
        },
        "name": "Llama 3.2 3B",
        "modelSource": "https://huggingface.co/meta-llama/Llama-3.2-3B",
        "offline": false,
        "traits": [
          "fastest"
        ]
      },
      "object": "model",
      "owned_by": "venice.ai",
      "type": "text"
    },
    {
      "created": 1733768349,
      "id": "llama-3.3-70b",
      "model_spec": {
        "pricing": {
          "input": {
            "usd": 0.7,
            "diem": 0.7
          },
          "output": {
            "usd": 2.8,
            "diem": 2.8
          }
        },
        "availableContextTokens": 131072,
        "capabilities": {
          "optimizedForCode": false,
          "quantization": "fp8",
          "supportsFunctionCalling": true,
          "supportsReasoning": false,
          "supportsResponseSchema": false,
          "supportsVision": false,
          "supportsWebSearch": true,
          "supportsLogProbs": false
        },
        "constraints": {
          "temperature": {
            "default": 0.6
          },
          "top_p": {
            "default": 0.95
          }
        },
        "name": "Llama 3.3 70B",
        "modelSource": "https://huggingface.co/meta-llama/Llama-3.3-70B-Instruct",
        "offline": false,
        "traits": [
          "function_calling_default",
          "default"
        ]
      },
      "object": "model",
      "owned_by": "venice.ai",
      "type": "text"
    }
  ],
  "image": [
    {
      "created": 1743099022,
      "id": "venice-sd35",
      "model_spec": {
        "pricing": {
          "generation": {
            "usd": 0.01,
            "diem": 0.01
          },
          "upscale": {
            "2x": {
              "usd": 0.02,
              "diem": 0.02
            },
            "4x": {
              "usd": 0.08,
              "diem": 0.08
            }
          }
        },
        "constraints": {
          "promptCharacterLimit": 1500,
          "steps": {
            "default": 25,
            "max": 30
          },
          "widthHeightDivisor": 16
        },
        "supportsWebSearch": false,
        "name": "Venice SD35",
        "modelSource": "https://huggingface.co/stabilityai/stable-diffusion-3.5-large",
        "offline": false,
        "traits": [
          "default",
          "eliza-default"
        ]
      },
      "object": "model",
      "owned_by": "venice.ai",
      "type": "image"
    },
    {
      "created": 1747080729,
      "id": "hidream",
      "model_spec": {
        "pricing": {
          "generation": {
            "usd": 0.01,
            "diem": 0.01
          },
          "upscale": {
            "2x": {
              "usd": 0.02,
              "diem": 0.02
            },
            "4x": {
              "usd": 0.08,
              "diem": 0.08
            }
          }
        },
        "constraints": {
          "promptCharacterLimit": 1500,
          "steps": {
            "default": 20,
            "max": 50
          },
          "widthHeightDivisor": 8
        },
        "supportsWebSearch": false,
        "name": "HiDream",
        "modelSource": "https://huggingface.co/HiDream-ai/HiDream-I1-Dev",
        "offline": false,
        "traits": []
      },
      "object": "model",
      "owned_by": "venice.ai",
      "type": "image"
    },
    {
      "created": 1763653951,
      "id": "nano-banana-pro",
      "model_spec": {
        "pricing": {
          "generation": {
            "usd": 0.18,
            "diem": 0.18
          },
          "upscale": {
            "2x": {
              "usd": 0.02,
              "diem": 0.02
            },
            "4x": {
              "usd": 0.08,
              "diem": 0.08
            }
          }
        },
        "constraints": {
          "promptCharacterLimit": 32768,
          "steps": {
            "default": 20,
            "max": 50
          },
          "widthHeightDivisor": 1
        },
        "supportsWebSearch": true,
        "name": "Nano Banana Pro",
        "offline": false,
        "traits": []
      },
      "object": "model",
      "owned_by": "venice.ai",
      "type": "image"
    },
    {
      "created": 1738704152,
      "id": "lustify-sdxl",
      "model_spec": {
        "pricing": {
          "generation": {
            "usd": 0.01,
            "diem": 0.01
          },
          "upscale": {
            "2x": {
              "usd": 0.02,
              "diem": 0.02
            },
            "4x": {
              "usd": 0.08,
              "diem": 0.08
            }
          }
        },
        "constraints": {
          "promptCharacterLimit": 1500,
          "steps": {
            "default": 20,
            "max": 50
          },
          "widthHeightDivisor": 8
        },
        "supportsWebSearch": false,
        "name": "Lustify SDXL",
        "modelSource": "https://civitai.com/models/573152/lustify-sdxl-nsfw-checkpoint",
        "offline": false,
        "traits": []
      },
      "object": "model",
      "owned_by": "venice.ai",
      "type": "image"
    },
    {
      "created": 1736635129,
      "id": "lustify-v7",
      "model_spec": {
        "pricing": {
          "generation": {
            "usd": 0.01,
            "diem": 0.01
          },
          "upscale": {
            "2x": {
              "usd": 0.02,
              "diem": 0.02
            },
            "4x": {
              "usd": 0.08,
              "diem": 0.08
            }
          }
        },
        "constraints": {
          "promptCharacterLimit": 1500,
          "steps": {
            "default": 20,
            "max": 50
          },
          "widthHeightDivisor": 8
        },
        "supportsWebSearch": false,
        "name": "Lustify v7",
        "modelSource": "https://civitai.com/models/573152/lustify-sdxl-nsfw-checkpoint",
        "offline": false,
        "traits": []
      },
      "object": "model",
      "owned_by": "venice.ai",
      "type": "image"
    },
    {
      "created": 1736635129,
      "id": "qwen-image",
      "model_spec": {
        "pricing": {
          "generation": {
            "usd": 0.01,
            "diem": 0.01
          },
          "upscale": {
            "2x": {
              "usd": 0.02,
              "diem": 0.02
            },
            "4x": {
              "usd": 0.08,
              "diem": 0.08
            }
          }
        },
        "constraints": {
          "promptCharacterLimit": 1500,
          "steps": {
            "default": 8,
            "max": 8
          },
          "widthHeightDivisor": 8
        },
        "supportsWebSearch": false,
        "name": "Qwen Image",
        "modelSource": "https://huggingface.co/Qwen/Qwen-Image",
        "offline": false,
        "traits": [
          "highest_quality"
        ]
      },
      "object": "model",
      "owned_by": "venice.ai",
      "type": "image"
    },
    {
      "created": 1736635129,
      "id": "wai-Illustrious",
      "model_spec": {
        "pricing": {
          "generation": {
            "usd": 0.01,
            "diem": 0.01
          },
          "upscale": {
            "2x": {
              "usd": 0.02,
              "diem": 0.02
            },
            "4x": {
              "usd": 0.08,
              "diem": 0.08
            }
          }
        },
        "constraints": {
          "promptCharacterLimit": 1500,
          "steps": {
            "default": 25,
            "max": 30
          },
          "widthHeightDivisor": 16
        },
        "supportsWebSearch": false,
        "name": "Anime (WAI)",
        "modelSource": "https://civitai.com/models/827184?modelVersionId=1761560",
        "offline": false,
        "traits": []
      },
      "object": "model",
      "owned_by": "venice.ai",
      "type": "image"
    },
    {
      "created": 1764758779,
      "id": "z-image-turbo",
      "model_spec": {
        "pricing": {
          "generation": {
            "usd": 0.01,
            "diem": 0.01
          },
          "upscale": {
            "2x": {
              "usd": 0.02,
              "diem": 0.02
            },
            "4x": {
              "usd": 0.08,
              "diem": 0.08
            }
          }
        },
        "constraints": {
          "promptCharacterLimit": 7500,
          "steps": {
            "default": 8,
            "max": 8
          },
          "widthHeightDivisor": 8
        },
        "supportsWebSearch": false,
        "name": "Z-Image Turbo",
        "modelSource": "https://huggingface.co/Tongyi-MAI/Z-Image-Turbo",
        "offline": false,
        "traits": []
      },
      "object": "model",
      "owned_by": "venice.ai",
      "type": "image"
    }
  ],
  "video": [
    {
      "created": 1758825748,
      "id": "wan-2.5-preview-image-to-video",
      "model_spec": {
        "privacy": "anonymized",
        "constraints": {
          "model_type": "image-to-video",
          "aspect_ratios": [],
          "resolutions": [
            "1080p",
            "720p",
            "480p"
          ],
          "durations": [
            "5s",
            "10s"
          ],
          "audio": true,
          "audio_configurable": false
        },
        "name": "Wan 2.5 Preview",
        "offline": false,
        "traits": []
      },
      "object": "model",
      "owned_by": "venice.ai",
      "type": "video"
    },
    {
      "created": 1758825748,
      "id": "wan-2.5-preview-text-to-video",
      "model_spec": {
        "privacy": "anonymized",
        "constraints": {
          "model_type": "text-to-video",
          "aspect_ratios": [],
          "resolutions": [
            "1080p",
            "720p",
            "480p"
          ],
          "durations": [
            "5s",
            "10s"
          ],
          "audio": true,
          "audio_configurable": false
        },
        "name": "Wan 2.5 Preview",
        "offline": false,
        "traits": []
      },
      "object": "model",
      "owned_by": "venice.ai",
      "type": "video"
    },
    {
      "created": 1758825748,
      "id": "wan-2.2-a14b-text-to-video",
      "model_spec": {
        "privacy": "private",
        "constraints": {
          "model_type": "text-to-video",
          "aspect_ratios": [
            "16:9",
            "9:16",
            "1:1"
          ],
          "resolutions": [
            "720p",
            "580p",
            "480p"
          ],
          "durations": [
            "5s"
          ],
          "audio": false,
          "audio_configurable": false
        },
        "name": "Wan 2.2 A14B",
        "offline": false,
        "traits": []
      },
      "object": "model",
      "owned_by": "venice.ai",
      "type": "video"
    },
    {
      "created": 1758825748,
      "id": "wan-2.1-pro-image-to-video",
      "model_spec": {
        "privacy": "private",
        "constraints": {
          "model_type": "image-to-video",
          "aspect_ratios": [
            "16:9"
          ],
          "resolutions": [],
          "durations": [
            "6s"
          ],
          "audio": false,
          "audio_configurable": false
        },
        "name": "Wan 2.1 Pro",
        "offline": false,
        "traits": []
      },
      "object": "model",
      "owned_by": "venice.ai",
      "type": "video"
    },
    {
      "created": 1765503106,
      "id": "ltx-2-fast-image-to-video",
      "model_spec": {
        "privacy": "anonymized",
        "constraints": {
          "model_type": "image-to-video",
          "aspect_ratios": [
            "16:9"
          ],
          "resolutions": [
            "1080p",
            "1440p",
            "2160p"
          ],
          "durations": [
            "6s",
            "8s",
            "10s",
            "12s",
            "14s",
            "16s",
            "18s",
            "20s"
          ],
          "audio": true,
          "audio_configurable": true
        },
        "name": "LTX Video 2.0 Fast",
        "offline": false,
        "traits": []
      },
      "object": "model",
      "owned_by": "venice.ai",
      "type": "video"
    },
    {
      "created": 1765503106,
      "id": "ltx-2-fast-text-to-video",
      "model_spec": {
        "privacy": "anonymized",
        "constraints": {
          "model_type": "text-to-video",
          "aspect_ratios": [
            "16:9"
          ],
          "resolutions": [
            "1080p",
            "1440p",
            "2160p"
          ],
          "durations": [
            "6s",
            "8s",
            "10s",
            "12s",
            "14s",
            "16s",
            "18s",
            "20s"
          ],
          "audio": true,
          "audio_configurable": true
        },
        "name": "LTX Video 2.0 Fast",
        "offline": false,
        "traits": []
      },
      "object": "model",
      "owned_by": "venice.ai",
      "type": "video"
    },
    {
      "created": 1765503106,
      "id": "ltx-2-full-image-to-video",
      "model_spec": {
        "privacy": "anonymized",
        "constraints": {
          "model_type": "image-to-video",
          "aspect_ratios": [
            "16:9"
          ],
          "resolutions": [
            "1080p",
            "1440p",
            "2160p"
          ],
          "durations": [
            "6s",
            "8s",
            "10s"
          ],
          "audio": true,
          "audio_configurable": true
        },
        "name": "LTX Video 2.0 Full Quality",
        "offline": false,
        "traits": []
      },
      "object": "model",
      "owned_by": "venice.ai",
      "type": "video"
    },
    {
      "created": 1765503106,
      "id": "ltx-2-full-text-to-video",
      "model_spec": {
        "privacy": "anonymized",
        "constraints": {
          "model_type": "text-to-video",
          "aspect_ratios": [
            "16:9"
          ],
          "resolutions": [
            "1080p",
            "1440p",
            "2160p"
          ],
          "durations": [
            "6s",
            "8s",
            "10s"
          ],
          "audio": true,
          "audio_configurable": true
        },
        "name": "LTX Video 2.0 Full Quality",
        "offline": false,
        "traits": []
      },
      "object": "model",
      "owned_by": "venice.ai",
      "type": "video"
    },
    {
      "created": 1758825748,
      "id": "ovi-image-to-video",
      "model_spec": {
        "privacy": "private",
        "constraints": {
          "model_type": "image-to-video",
          "aspect_ratios": [],
          "resolutions": [],
          "durations": [
            "5s"
          ],
          "audio": true,
          "audio_configurable": false
        },
        "name": "Ovi",
        "modelSource": "https://huggingface.co/chetwinlow1/Ovi",
        "offline": false,
        "traits": []
      },
      "object": "model",
      "owned_by": "venice.ai",
      "type": "video"
    },
    {
      "created": 1765503106,
      "id": "kling-2.6-pro-text-to-video",
      "model_spec": {
        "privacy": "anonymized",
        "constraints": {
          "model_type": "text-to-video",
          "aspect_ratios": [
            "16:9",
            "9:16",
            "1:1"
          ],
          "resolutions": [],
          "durations": [
            "5s",
            "10s"
          ],
          "audio": true,
          "audio_configurable": true
        },
        "name": "Kling 2.6 Pro",
        "offline": false,
        "traits": []
      },
      "object": "model",
      "owned_by": "venice.ai",
      "type": "video"
    },
    {
      "created": 1765503106,
      "id": "kling-2.6-pro-image-to-video",
      "model_spec": {
        "privacy": "anonymized",
        "constraints": {
          "model_type": "image-to-video",
          "aspect_ratios": [],
          "resolutions": [],
          "durations": [
            "5s",
            "10s"
          ],
          "audio": true,
          "audio_configurable": true
        },
        "name": "Kling 2.6 Pro",
        "offline": false,
        "traits": []
      },
      "object": "model",
      "owned_by": "venice.ai",
      "type": "video"
    },
    {
      "created": 1758825748,
      "id": "kling-2.5-turbo-pro-text-to-video",
      "model_spec": {
        "privacy": "anonymized",
        "constraints": {
          "model_type": "text-to-video",
          "aspect_ratios": [
            "16:9",
            "9:16",
            "1:1"
          ],
          "resolutions": [],
          "durations": [
            "5s",
            "10s"
          ],
          "audio": false,
          "audio_configurable": false
        },
        "name": "Kling 2.5 Turbo Pro",
        "offline": false,
        "traits": []
      },
      "object": "model",
      "owned_by": "venice.ai",
      "type": "video"
    },
    {
      "created": 1758825748,
      "id": "kling-2.5-turbo-pro-image-to-video",
      "model_spec": {
        "privacy": "anonymized",
        "constraints": {
          "model_type": "image-to-video",
          "aspect_ratios": [],
          "resolutions": [],
          "durations": [
            "5s",
            "10s"
          ],
          "audio": false,
          "audio_configurable": false
        },
        "name": "Kling 2.5 Turbo Pro",
        "offline": false,
        "traits": []
      },
      "object": "model",
      "owned_by": "venice.ai",
      "type": "video"
    },
    {
      "created": 1764806400,
      "id": "longcat-distilled-image-to-video",
      "model_spec": {
        "privacy": "private",
        "constraints": {
          "model_type": "image-to-video",
          "aspect_ratios": [],
          "resolutions": [
            "720p"
          ],
          "durations": [
            "5s",
            "10s",
            "15s",
            "20s",
            "30s"
          ],
          "audio": false,
          "audio_configurable": false
        },
        "name": "Longcat Distilled",
        "modelSource": "https://huggingface.co/meituan-longcat/LongCat-Video",
        "offline": false,
        "traits": []
      },
      "object": "model",
      "owned_by": "venice.ai",
      "type": "video"
    },
    {
      "created": 1764806400,
      "id": "longcat-distilled-text-to-video",
      "model_spec": {
        "privacy": "private",
        "constraints": {
          "model_type": "text-to-video",
          "aspect_ratios": [
            "16:9",
            "9:16",
            "1:1"
          ],
          "resolutions": [
            "720p"
          ],
          "durations": [
            "5s",
            "10s",
            "15s",
            "20s",
            "30s"
          ],
          "audio": false,
          "audio_configurable": false
        },
        "name": "Longcat Distilled",
        "modelSource": "https://huggingface.co/meituan-longcat/LongCat-Video",
        "offline": false,
        "traits": []
      },
      "object": "model",
      "owned_by": "venice.ai",
      "type": "video"
    },
    {
      "created": 1764806400,
      "id": "longcat-image-to-video",
      "model_spec": {
        "privacy": "private",
        "constraints": {
          "model_type": "image-to-video",
          "aspect_ratios": [],
          "resolutions": [
            "720p"
          ],
          "durations": [
            "5s",
            "10s",
            "15s",
            "20s",
            "30s"
          ],
          "audio": false,
          "audio_configurable": false
        },
        "name": "Longcat Full Quality",
        "modelSource": "https://huggingface.co/meituan-longcat/LongCat-Video",
        "offline": false,
        "traits": []
      },
      "object": "model",
      "owned_by": "venice.ai",
      "type": "video"
    },
    {
      "created": 1764806400,
      "id": "longcat-text-to-video",
      "model_spec": {
        "privacy": "private",
        "constraints": {
          "model_type": "text-to-video",
          "aspect_ratios": [
            "16:9",
            "9:16",
            "1:1"
          ],
          "resolutions": [
            "720p"
          ],
          "durations": [
            "5s",
            "10s",
            "15s",
            "20s",
            "30s"
          ],
          "audio": false,
          "audio_configurable": false
        },
        "name": "Longcat Full Quality",
        "modelSource": "https://huggingface.co/meituan-longcat/LongCat-Video",
        "offline": false,
        "traits": []
      },
      "object": "model",
      "owned_by": "venice.ai",
      "type": "video"
    },
    {
      "created": 1758825748,
      "id": "veo3-fast-text-to-video",
      "model_spec": {
        "privacy": "anonymized",
        "constraints": {
          "model_type": "text-to-video",
          "aspect_ratios": [
            "16:9",
            "9:16",
            "1:1"
          ],
          "resolutions": [
            "720p",
            "1080p"
          ],
          "durations": [
            "4s",
            "6s",
            "8s"
          ],
          "audio": true,
          "audio_configurable": false
        },
        "name": "Veo 3 Fast",
        "offline": false,
        "traits": []
      },
      "object": "model",
      "owned_by": "venice.ai",
      "type": "video"
    },
    {
      "created": 1758825748,
      "id": "veo3-fast-image-to-video",
      "model_spec": {
        "privacy": "anonymized",
        "constraints": {
          "model_type": "image-to-video",
          "aspect_ratios": [
            "16:9"
          ],
          "resolutions": [],
          "durations": [
            "8s"
          ],
          "audio": true,
          "audio_configurable": false
        },
        "name": "Veo 3 Fast",
        "offline": false,
        "traits": []
      },
      "object": "model",
      "owned_by": "venice.ai",
      "type": "video"
    },
    {
      "created": 1758825748,
      "id": "veo3-full-text-to-video",
      "model_spec": {
        "privacy": "anonymized",
        "constraints": {
          "model_type": "text-to-video",
          "aspect_ratios": [
            "16:9",
            "9:16"
          ],
          "resolutions": [
            "720p",
            "1080p"
          ],
          "durations": [
            "4s",
            "6s",
            "8s"
          ],
          "audio": true,
          "audio_configurable": false
        },
        "name": "Veo 3 Full Quality",
        "offline": false,
        "traits": []
      },
      "object": "model",
      "owned_by": "venice.ai",
      "type": "video"
    },
    {
      "created": 1758825748,
      "id": "veo3-full-image-to-video",
      "model_spec": {
        "privacy": "anonymized",
        "constraints": {
          "model_type": "image-to-video",
          "aspect_ratios": [
            "16:9"
          ],
          "resolutions": [],
          "durations": [
            "8s"
          ],
          "audio": true,
          "audio_configurable": false
        },
        "name": "Veo 3 Full Quality",
        "offline": false,
        "traits": []
      },
      "object": "model",
      "owned_by": "venice.ai",
      "type": "video"
    },
    {
      "created": 1765503106,
      "id": "veo3.1-fast-text-to-video",
      "model_spec": {
        "privacy": "anonymized",
        "constraints": {
          "model_type": "text-to-video",
          "aspect_ratios": [
            "16:9",
            "9:16",
            "1:1"
          ],
          "resolutions": [
            "720p",
            "1080p"
          ],
          "durations": [
            "4s",
            "6s",
            "8s"
          ],
          "audio": true,
          "audio_configurable": true
        },
        "name": "Veo 3.1 Fast",
        "offline": false,
        "traits": []
      },
      "object": "model",
      "owned_by": "venice.ai",
      "type": "video"
    },
    {
      "created": 1765503106,
      "id": "veo3.1-fast-image-to-video",
      "model_spec": {
        "privacy": "anonymized",
        "constraints": {
          "model_type": "image-to-video",
          "aspect_ratios": [
            "16:9",
            "9:16"
          ],
          "resolutions": [
            "720p",
            "1080p"
          ],
          "durations": [
            "8s"
          ],
          "audio": true,
          "audio_configurable": true
        },
        "name": "Veo 3.1 Fast",
        "offline": false,
        "traits": []
      },
      "object": "model",
      "owned_by": "venice.ai",
      "type": "video"
    },
    {
      "created": 1765503106,
      "id": "veo3.1-full-text-to-video",
      "model_spec": {
        "privacy": "anonymized",
        "constraints": {
          "model_type": "text-to-video",
          "aspect_ratios": [
            "16:9",
            "9:16",
            "1:1"
          ],
          "resolutions": [
            "720p",
            "1080p"
          ],
          "durations": [
            "4s",
            "6s",
            "8s"
          ],
          "audio": true,
          "audio_configurable": true
        },
        "name": "Veo 3.1 Full Quality",
        "offline": false,
        "traits": []
      },
      "object": "model",
      "owned_by": "venice.ai",
      "type": "video"
    },
    {
      "created": 1765503106,
      "id": "veo3.1-full-image-to-video",
      "model_spec": {
        "privacy": "anonymized",
        "constraints": {
          "model_type": "image-to-video",
          "aspect_ratios": [
            "16:9",
            "9:16"
          ],
          "resolutions": [
            "720p",
            "1080p"
          ],
          "durations": [
            "8s"
          ],
          "audio": true,
          "audio_configurable": true
        },
        "name": "Veo 3.1 Full Quality",
        "offline": false,
        "traits": []
      },
      "object": "model",
      "owned_by": "venice.ai",
      "type": "video"
    },
    {
      "created": 1758825748,
      "id": "sora-2-image-to-video",
      "model_spec": {
        "privacy": "anonymized",
        "constraints": {
          "model_type": "image-to-video",
          "aspect_ratios": [
            "16:9",
            "9:16"
          ],
          "resolutions": [
            "720p"
          ],
          "durations": [
            "4s",
            "8s",
            "12s"
          ],
          "audio": true,
          "audio_configurable": false
        },
        "name": "Sora 2",
        "offline": false,
        "traits": []
      },
      "object": "model",
      "owned_by": "venice.ai",
      "type": "video"
    },
    {
      "created": 1758825748,
      "id": "sora-2-pro-image-to-video",
      "model_spec": {
        "privacy": "anonymized",
        "constraints": {
          "model_type": "image-to-video",
          "aspect_ratios": [
            "16:9",
            "9:16"
          ],
          "resolutions": [
            "720p",
            "1080p"
          ],
          "durations": [
            "4s",
            "8s",
            "12s"
          ],
          "audio": true,
          "audio_configurable": false
        },
        "name": "Sora 2 Pro",
        "offline": false,
        "traits": []
      },
      "object": "model",
      "owned_by": "venice.ai",
      "type": "video"
    },
    {
      "created": 1758825748,
      "id": "sora-2-text-to-video",
      "model_spec": {
        "privacy": "anonymized",
        "constraints": {
          "model_type": "text-to-video",
          "aspect_ratios": [
            "16:9",
            "9:16"
          ],
          "resolutions": [
            "720p"
          ],
          "durations": [
            "4s",
            "8s",
            "12s"
          ],
          "audio": true,
          "audio_configurable": false
        },
        "name": "Sora 2",
        "offline": false,
        "traits": []
      },
      "object": "model",
      "owned_by": "venice.ai",
      "type": "video"
    },
    {
      "created": 1758825748,
      "id": "sora-2-pro-text-to-video",
      "model_spec": {
        "privacy": "anonymized",
        "constraints": {
          "model_type": "text-to-video",
          "aspect_ratios": [
            "16:9",
            "9:16"
          ],
          "resolutions": [
            "720p",
            "1080p"
          ],
          "durations": [
            "4s",
            "8s",
            "12s"
          ],
          "audio": true,
          "audio_configurable": false
        },
        "name": "Sora 2 Pro",
        "offline": false,
        "traits": []
      },
      "object": "model",
      "owned_by": "venice.ai",
      "type": "video"
    }
  ],
  "embedding": [
    {
      "created": 1741924661,
      "id": "text-embedding-bge-m3",
      "model_spec": {
        "pricing": {
          "input": {
            "usd": 0.15,
            "diem": 0.15
          },
          "output": {
            "usd": 0.6,
            "diem": 0.6
          }
        },
        "name": "BGE-M3",
        "modelSource": "https://huggingface.co/BAAI/bge-m3",
        "offline": false,
        "traits": []
      },
      "object": "model",
      "owned_by": "venice.ai",
      "type": "embedding"
    }
  ],
  "tts": [
    {
      "created": 1742418046,
      "id": "tts-kokoro",
      "model_spec": {
        "pricing": {
          "input": {
            "usd": 3.5,
            "diem": 3.5
          }
        },
        "voices": [
          "af_alloy",
          "af_aoede",
          "af_bella",
          "af_heart",
          "af_jadzia",
          "af_jessica",
          "af_kore",
          "af_nicole",
          "af_nova",
          "af_river",
          "af_sarah",
          "af_sky",
          "am_adam",
          "am_echo",
          "am_eric",
          "am_fenrir",
          "am_liam",
          "am_michael",
          "am_onyx",
          "am_puck",
          "am_santa",
          "bf_alice",
          "bf_emma",
          "bf_lily",
          "bm_daniel",
          "bm_fable",
          "bm_george",
          "bm_lewis",
          "ef_dora",
          "em_alex",
          "em_santa",
          "ff_siwis",
          "hf_alpha",
          "hf_beta",
          "hm_omega",
          "hm_psi",
          "if_sara",
          "im_nicola",
          "jf_alpha",
          "jf_gongitsune",
          "jf_nezumi",
          "jf_tebukuro",
          "jm_kumo",
          "pf_dora",
          "pm_alex",
          "pm_santa",
          "zf_xiaobei",
          "zf_xiaoni",
          "zf_xiaoxiao",
          "zf_xiaoyi",
          "zm_yunjian",
          "zm_yunxi",
          "zm_yunxia",
          "zm_yunyang"
        ],
        "name": "Kokoro Text to Speech",
        "modelSource": "https://huggingface.co/hexgrad/Kokoro-82M",
        "offline": false,
        "traits": []
      },
      "object": "model",
      "owned_by": "venice.ai",
      "type": "tts"
    }
  ],
  "upscale": [
    {
      "created": 1744453050,
      "id": "upscaler",
      "model_spec": {
        "pricing": {
          "generation": {
            "usd": 0.01,
            "diem": 0.01
          },
          "upscale": {
            "2x": {
              "usd": 0.02,
              "diem": 0.02
            },
            "4x": {
              "usd": 0.08,
              "diem": 0.08
            }
          }
        },
        "name": "Upscaler",
        "offline": false,
        "traits": []
      },
      "object": "model",
      "owned_by": "venice.ai",
      "type": "upscale"
    }
  ]
};