from nltk.corpus import wordnet as wn

def get_hierarchy(word, pos='n', lang='arb'):
    """
    Get the hypernym and hyponym hierarchy for a given word.
    
    Args:
        word (str): The word to query.
        pos (str): Part of speech (default is 'n' for noun).
        lang (str): Language code (default is 'arb' for Arabic).
    
    Returns:
        dict: A dictionary containing 'hypernyms' and 'hyponyms'.
    """
    synsets = wn.synsets(word, pos=pos, lang=lang)
    if not synsets:
        return {"hypernyms": ["Error: no synsets"], "hyponyms": ["Error: no synsets"]}
    
    # Initialize hierarchy
    hierarchy = {"hypernyms": [], "hyponyms": []}
    
    # Get the most common synset
    current_synset = synsets[0]
    
    # Traverse hypernyms (up the hierarchy)
    while current_synset:
        hierarchy["hypernyms"].append(current_synset.name())
        hypernyms = current_synset.hypernyms()
        if not hypernyms:
            break
        current_synset = hypernyms[0]  # Move up the hierarchy
    
    # Traverse hyponyms (down the hierarchy)
    current_synset = synsets[0]
    stack = [current_synset]
    while stack:
        current = stack.pop()
        hierarchy["hyponyms"].append(current.name())
        hyponyms = current.hyponyms()
        stack.extend(hyponyms)  # Add hyponyms to the stack for further traversal
    
    return hierarchy

# Example usage
word = 'سمع_الدعوى'
hierarchy = get_hierarchy(word, lang='arb')
print(f"Hierarchy for '{word}': {hierarchy['hypernyms']}")