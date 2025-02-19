records = {}

if __name__ == '__main__':
    for _ in range(int(input())):
        name = input()
        score = float(input())
        records[name] = score

s = set()
for score in records.values():
    s.add(score)

unique_scores = sorted(list(s))
ordered_records = dict(sorted(records.items()))

for name, score in ordered_records.items():
    if score == unique_scores[1]:
        print(name)
