"""
This code sample shows Prebuilt Layout operations with the Azure Form Recognizer client library. 
The async versions of the samples require Python 3.6 or later.

To learn more, please visit the documentation - Quickstart: Form Recognizer Python client library SDKs
https://learn.microsoft.com/azure/applied-ai-services/form-recognizer/quickstarts/get-started-v3-sdk-rest-api?view=doc-intel-3.1.0&pivots=programming-language-python
"""

from azure.core.credentials import AzureKeyCredential
# from azure.ai.formrecognizer import DocumentAnalysisClient
from azure.ai.documentintelligence import DocumentIntelligenceClient
from azure.ai.documentintelligence.models import AnalyzeDocumentRequest, AnalyzeResult
import os
import base64
from dotenv import load_dotenv
load_dotenv('.env')

"""
Remember to remove the key from your code when you're done, and never post it publicly. For production, use
secure methods to store and access your credentials. For more information, see 
https://docs.microsoft.com/en-us/azure/cognitive-services/cognitive-services-security?tabs=command-line%2Ccsharp#environment-variables-and-application-configuration
"""
endpoint = os.environ["FORM_RECOGNIZER_ENDPOINT"]
key = os.environ["FORM_RECOGNIZER_KEY"]
path_to_sample_documents = "sample-layout.docx"
# path_to_sample_documents = "sample-layout.pdf"

# sample document
formUrl = "https://raw.githubusercontent.com/Azure-Samples/cognitive-services-REST-api-samples/master/curl/form-recognizer/sample-layout.pdf"

document_analysis_client = DocumentIntelligenceClient(
    endpoint=endpoint, credential=AzureKeyCredential(key)
)
    
# poller = document_analysis_client.begin_analyze_document("prebuilt-layout", analyze_request=formUrl)
with open(path_to_sample_documents, "rb") as f:
    poller = document_analysis_client.begin_analyze_document(
        "prebuilt-layout", analyze_request=f, content_type="application/octet-stream", output_content_format="markdown"
    )
# with open(path_to_sample_documents, "rb") as f:
#     encoded_file = base64.b64encode(f.read()).decode("utf-8")
#     poller = document_analysis_client.begin_analyze_document(
#         "prebuilt-layout", analyze_request={"base64Source": encoded_file}, output_content_format="markdown"
#     )
# with open(path_to_sample_documents, "rb") as f:
#     encoded_file = base64.b64encode(f.read())
#     poller = document_analysis_client.begin_analyze_document(
#         "prebuilt-layout", AnalyzeDocumentRequest(base64_source=encoded_file), output_content_format="markdown"
#     )

# docUrl = "https://documentintelligence.ai.azure.com/documents/samples/layout/layout-pageobject.pdf"
# poller = document_analysis_client.begin_analyze_document(
#     "prebuilt-layout", AnalyzeDocumentRequest(url_source=docUrl), output_content_format="markdown"
# )
# with open(path_to_sample_documents, "rb") as f:
#     encoded_file = base64.b64encode(f.read()).decode("utf-8")
#     poller = document_analysis_client.begin_analyze_document(
#         "prebuilt-layout", analyze_request=encoded_file,  output_content_format="markdown"
#     )

result: AnalyzeResult = poller.result()
print(result.content)

# for idx, style in enumerate(result.styles):
#     print(
#         "Document contains {} content".format(
#          "handwritten" if style.is_handwritten else "no handwritten"
#         )
#     )

# for page in result.pages:
#     for line_idx, line in enumerate(page.lines):
#         print(
#          "...Line # {} has text content '{}'".format(
#         line_idx,
#         line.content.encode("utf-8")
#         )
#     )

#     for selection_mark in page.selection_marks:
#         print(
#          "...Selection mark is '{}' and has a confidence of {}".format(
#          selection_mark.state,
#          selection_mark.confidence
#          )
#     )

# for table_idx, table in enumerate(result.tables):
#     print(
#         "Table # {} has {} rows and {} columns".format(
#         table_idx, table.row_count, table.column_count
#         )
#     )
        
#     for cell in table.cells:
#         print(
#             "...Cell[{}][{}] has content '{}'".format(
#             cell.row_index,
#             cell.column_index,
#             cell.content.encode("utf-8"),
#             )
#         )

print("----------------------------------------")

