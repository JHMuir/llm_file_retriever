import os
import dspy

class FileRetreiverSignature(dspy.Signature):
    """
    Given a list of available relative file paths within a designated directory
    and a user request, identify the specific relative file path the user wants.
    Respond ONLY with the relative path identified from the context.
    If no single file clearly matches, respond with 'NOT_FOUND'.
    """
    directory: list[str] = dspy.InputField(desc="A list of relative file paths available from a given directory")
    request: str = dspy.InputField(desc="The user's natural language request for a file")
    
    identified_relative_path: str = dspy.OutputField(desc="A single relative file path identified from the context that best matches the user request, or 'NOT FOUND'")
    
class FileRetrieverModule(dspy.Module):
    def __init__(self):
        super().__init__()
        self.signature = dspy.Predict(FileRetreiverSignature)
        
    def forward(self, directory, request):
        predicted_file = self.signature(directory=directory, request=request)
        return predicted_file