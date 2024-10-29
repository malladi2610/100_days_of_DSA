import re
from datetime import datetime

def calculate_performance_rate(readme_content):
    # Find all days listed in the "Done Nothing" section
    done_nothing_days = re.findall(r'<li>Day \d+(?: - Day \d+)?</li>', readme_content)
    done_nothing_days_set = set()

    for day in done_nothing_days:
        day = day.replace('<li>Day ', '').replace('</li>', '')
        if ' - ' in day:
            start, end = map(int, day.split(' - '))
            done_nothing_days_set.update(range(start, end + 1))
        else:
            done_nothing_days_set.add(int(day))

    # Debug statement for done nothing days count
    print(f"Done Nothing Days Count: {len(done_nothing_days_set)}")

    # Find all days listed in the "Done" section
    done_days = re.findall(r'- \*\*Day \d+\*\*', readme_content)
    done_days_set = {int(re.search(r'\d+', day).group()) for day in done_days}

    # Debug statement for done days count
    print(f"Done Days Count: {len(done_days_set)}")

    # Calculate total days based on the highest day number
    total_days = max(done_nothing_days_set.union(done_days_set))

    # Debug statement for total days
    print(f"Total Days: {total_days}")

    if total_days == 0:
        return 0
    performance_rate = (len(done_days_set) / total_days) * 100

    # Debug statement for performance rate
    print(f"Performance Rate: {performance_rate}")

    return performance_rate

def update_readme(readme_path):
    with open(readme_path, 'r', encoding='utf-8') as file:
        content = file.read()

    performance_rate = calculate_performance_rate(content)
    last_updated = datetime.now().strftime('%d-%m-%Y')

    # Debug statement for last updated date
    print(f"Last Updated: {last_updated}")

    new_content = re.sub(
        r'\*\*Effective Performance Rate: No\.of Done days/Total No\.of days = \d+% \[Last updated: \d{2}-\d{2}-\d{4}\]\*\*',
        f'**Effective Performance Rate: No.of Done days/Total No.of days = {int(performance_rate)}% [Last updated: {last_updated}]**',
        content
    )

    # Debug statement for new content
    print("New Content:\n", new_content)

    with open(readme_path, 'w', encoding='utf-8') as file:
        file.write(new_content)

if __name__ == "__main__":
    update_readme('../README.md')