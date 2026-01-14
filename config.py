"""
Central configuration for Pegasus.
All tunable parameters should live here to avoid hardcoding.
"""

# ================================
# LLM Configuration
# ================================

# Primary Ollama model (must be available in your Ollama Cloud account)
PRIMARY_MODEL = "gpt-oss:120b"

# Safe fallback model if primary is unavailable
FALLBACK_MODEL = "llama3.1"

# Ollama host (Cloud)
OLLAMA_HOST = "https://ollama.com"


# ================================
# Research Parameters
# ================================

# Number of research vectors to generate
NUM_RESEARCH_VECTORS = 7

# Number of web sources per vector
MAX_SOURCES_PER_VECTOR = 3

# Maximum characters pulled from each source
MAX_CHARS_PER_SOURCE = 2000

# Maximum context passed to master synthesis
MAX_MASTER_CONTEXT_CHARS = 10000


# ================================
# Runtime / UX
# ================================

# Enable verbose logging (useful for debugging)
DEBUG_LOGGING = True
