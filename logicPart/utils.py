def rle_encode(s):
    if not s:
        return ""
    
    result = []
    count = 1
    
    for i in range(1, len(s)):
        if s[i] == s[i-1]:
            count += 1
        else:
            if count > 1:
                result.append(f"{count}{s[i-1]}")
            else:
                result.append(s[i-1])
            count = 1
    
    # Add the last group
    if count > 1:
        result.append(f"{count}{s[-1]}")
    else:
        result.append(s[-1])
    
    return ''.join(result)
