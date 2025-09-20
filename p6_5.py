import warnings
warnings.simplefilter("ignore", SyntaxError)
warnings.simplefilter("always", ImportWarning)
warnings.warn("Warning, no code here", SyntaxWarning)
warnings.warn("Warning, module not import", ImportWarning)









