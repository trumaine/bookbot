def get_num_words(text):
  words = text.split()
  return len(words)

def get_char_count(text):
  chars = {}
  for c in text:
    lowered = c.lower()
    if lowered in chars:
      chars[lowered] += 1
    else:
      chars[lowered] = 1
  return chars

def sort_on(d):
  return d["num"]

def chars_dict_to_sorted_list(char_dict):
  sorted_list = []
  for c in char_dict:
    sorted_list.append({"char": c, "num": char_dict[c]})
  sorted_list.sort(reverse=True, key=sort_on)
  return sorted_list
