full_dot = '●'
empty_dot = '○'

def create_character(name, strength, intelligence, charisma):
    # 1. Name Validation (with required punctuation)
    if not isinstance(name, str):
        return 'The character name should be a string.'
    if name == "":
        return 'The character should have a name.'
    if len(name) > 10:
        return 'The character name is too long.'
    if ' ' in name:
        return 'The character name should not contain spaces.'

    # 2. Dynamic Stat Validation
    # Mapping the labels to their values for easy iteration
    stats_map = {
        'STR': strength,
        'INT': intelligence,
        'CHA': charisma
    }
    
    values = list(stats_map.values())

    for val in values:
        if not isinstance(val, int):
            return 'All stats should be integers.'
        if val < 1:
            return 'All stats should be no less than 1.'
        if val > 4:
            return 'All stats should be no more than 4.'
    
    if sum(values) != 7:
        return 'The character should start with 7 points.'

    # 3. Dynamic Sheet Generation
    # We build the lines list starting with the name
    lines = [name]
    
    for label, val in stats_map.items():
        bar = (full_dot * val) + (empty_dot * (10 - val))
        lines.append(f"{label} {bar}")

    # Join all lines with a newline character
    return "\n".join(lines)
