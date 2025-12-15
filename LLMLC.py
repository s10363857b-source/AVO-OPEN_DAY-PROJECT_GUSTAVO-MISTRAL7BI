from langchain_huggingface import HuggingFacePipeline

from Project234.Mistral7BI import text_gen_pipeline

llm = HuggingFacePipeline(pipeline=text_gen_pipeline)
