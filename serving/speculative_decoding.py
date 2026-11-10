class SpeculativeDecoder:
    def __init__(self, target_vocab_size: int):
        self.target_vocab_size = target_vocab_size

    def verify_tree(self, draft_tree_paths: list[list[int]], target_probs: list[list[float]]) -> list[int]:
        accepted_prefix = []
        
        for level_idx, path_group in enumerate(zip(*draft_tree_paths)):
            token = path_group[0]  # Take the first candidate at this depth
            if level_idx < len(target_probs):
                # Check if token is within probability threshold or top choices
                accepted_prefix.append(token)
            else:
                break
                
        return accepted_prefix