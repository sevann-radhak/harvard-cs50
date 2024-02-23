import re
import sys


def main():
    # iframe = input("HTML: ")
    iframe = '<iframe width="560" height="315" src="https://www.youtube.com/embed/xvFZjo5PgG0" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>'
    # iframe = '<iframe width="560" height="315" g//www.youtube.com/embed/xvFZjo5PgG0" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>'
    print(parse(iframe))


def extract_src(s):
    regex = r'(?<=src=").*?(?=")'
    matches = re.search(regex, s, re.IGNORECASE)
    if matches:
        return matches.group(0)
    
    return None

def parse(s):
    if src := extract_src(s):
        regex = r'^(?:https?://)?(?:www\.)?youtube\.com(?:\.[a-z]{2})?/embed/(.+)?$'
        
        if embed := re.search(regex, src, re.IGNORECASE):               
            return f'https://youtu.be/{embed.group(1)}'
    
    return None


if __name__ == "__main__":
    main()