from mcp.server.fastmcp import FastMCP
from pydantic import BaseModel, Field

mcp = FastMCP("DocumentMCP", log_level="ERROR")


docs = {
    "deposition.md": "This deposition covers the testimony of Angela Smith, P.E.",
    "report.pdf": "The report details the state of a 20m condenser tower.",
    "financials.docx": "These financials outline the project's budget and expenditures.",
    "outlook.pdf": "This document presents the projected future performance of the system.",
    "plan.md": "The plan outlines the steps for the project's implementation.",
    "spec.txt": "These specifications define the technical requirements for the equipment.",
}


@mcp.tool(name="read_doc", description="Read a document and return the contents as a string")
def read_document(doc_id: str = Field(description="The ID of the document to read")) -> str:
    if doc_id not in docs:
        raise ValueError(f"Document with ID {doc_id} not found")
    return docs[doc_id]

@mcp.tool(name="edit_document", description="Edit a document by replacing the contents with the new content and return the contents as a string")
def edit_document(doc_id: str = Field(description="The ID of the document to edit"), old_content: str = Field(description="The old content to replace"), new_content: str = Field(description="The new content to write to the document")) -> str:
    if doc_id not in docs:
        raise ValueError(f"Document with ID {doc_id} not found")
    docs[doc_id] = new_content
    return docs[doc_id]

# TODO: Write a tool to read a doc
# TODO: Write a tool to edit a doc
# TODO: Write a resource to return all doc id's
# TODO: Write a resource to return the contents of a particular doc
# TODO: Write a prompt to rewrite a doc in markdown format
# TODO: Write a prompt to summarize a doc


if __name__ == "__main__":
    mcp.run(transport="stdio")
