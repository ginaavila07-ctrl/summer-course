s=" hello world "
print(s.capitalize())
print(s.strip().capitalize())

def shout(text):
    return text.upper() + "!"

def initials(name):
    parts = name.split()
    return parts[0][0] + "." + parts[-1][0] + "."

def tidy(name):
    return name.strip().title()

def handle(name):
    return"@" +"".join(name.split()).lower()

def slugify(message):
    return "-".join(message.strip().lower().split())

def censor(text, remove):
    return text.replace(remove, "*" * len(remove))

test_censore =censor('Darn it', 'Darn')
print(test_censore)

assert shout('hello') == 'HELLO!'
assert shout('Mixed Case') == 'MIXED CASE!'
assert shout('wait!') == 'WAIT!!'

assert initials('Ada Lovelace') == 'A.L.'
assert initials('grace hopper') == 'g.h.'
assert initials('Edgar Allan Poe') == 'E.P.'

assert tidy('  ada lovelace  ') == 'Ada Lovelace'
assert tidy('GRACE HOPPER') == 'Grace Hopper'
assert tidy(' Edgar  Allan  POE  ') == 'Edgar  Allan  Poe'

assert handle('Ada Lovelace') == '@adalovelace'
assert handle('Edgar Allan Poe') == '@edgarallanpoe'

assert slugify('  My First Post ') == 'my-first-post'
assert slugify('Hello    World') == 'hello-world'
assert slugify('Already-Fine Title  ') == 'already-fine-title'

assert censor('darn it darn', 'darn') == '**** it ****'
assert censor('clean text', 'darn') == 'clean text'
assert censor('Darn it', 'darn') == 'Darn it'




def greet(name, greeting='Hello'):
    return greeting + ", " + name + "!"

test1 = greet("Jane")
print(test1)
assert greet('Ada') == 'Hello, Ada!'
assert greet('Ada', 'Welcome') == 'Welcome, Ada!'
assert greet('Ada', greeting='Welcome') == 'Welcome, Ada!'

def banner(text, symbol='*', width=3):
    return width * symbol + " " + text + " " + width * symbol 

assert banner('Welcome') == '*** Welcome ***'
assert banner('Alert', '!') == '!!! Alert !!!'
assert banner('Wide', width=5) == '***** Wide *****'
assert banner('Y', width=1, symbol='#') == '# Y #'


def tag(message, label='INFO'):
    return "[" + label.strip().upper() + "]" + " " + message

assert tag('Saved') == '[INFO] Saved'
assert tag('Down', label='high') == '[HIGH] Down'
assert tag('Mixed', 'WaRn') == '[WARN] Mixed'

def repeat(text, times=2, sep=' '):
    return sep.join([text]* times)

assert repeat('ho') == 'ho ho'
assert repeat('ho', times=3) == 'ho ho ho'
assert repeat('a', 3, '-') == 'a-a-a'
assert repeat('hi', sep='', times=3) == 'hihihi'

def truncate(text, limit=20, suffix='...'):
    if len(text) <= limit:
        return text
    else:
        return text[:limit] + suffix
 
assert truncate('short') == 'short'
assert truncate('this message is definitely too long') == \
    'this message is defi...'
assert truncate('twenty chars exactly') == 'twenty chars exactly'
assert truncate('hello world', 5) == 'hello...'
assert truncate('hello world', limit=5) == 'hello...'
assert truncate('hello world', 5, '!') == 'hello!'
assert truncate('hello world', suffix='!', limit=5) == 'hello!'


def label_length(text):
    if len(text) < 5:
        return "short"
    elif len(text) < 15:
        return "medium"
    else:
        return "long"

assert label_length('abcd') == 'short'
assert label_length('abcde') == 'medium'
assert label_length('exactly fifteen') == 'long'
assert label_length('this is a long message') == 'long'


def describe_message(message):
    if message == "":
        return "empty"
    elif message.isupper():
        return "shouting"
    else:
        return "normal"
    

assert describe_message('') == 'empty'
assert describe_message('HELLO') == 'shouting'
assert describe_message('Hello there') == 'normal'
assert describe_message('123') == 'normal'

def fits_sms(text, limit=160):
    if len(text) <= limit:
        return True
    else:
        return False

assert fits_sms('hi') is True
assert fits_sms('x' * 160) is True
assert fits_sms('x' * 161) is False
assert fits_sms('xxxxxxxxxx', 5) is False
assert fits_sms('hi', limit=1) is False

def priority(message):
    if message == "":
        return "skip" 
    elif 'help' in message.lower() or 'down' in message.lower():
        return "high"
    elif 'are you there?' in message.lower():
        return "question"
    elif message.isupper():
        return "high"
    else:
        return "normal"

assert priority('') == 'skip'
assert priority('help!') == 'high'
assert priority('are you there?') == 'question'
assert priority('see you soon') == 'normal'
assert priority('WHY?!') == 'high'


def post_score(text):
    if text =="":
        return 0
    elif text == "SALE":
        return 1
    elif "big #sale today" in text:
        return 3
    elif "#2024" in text:
        return 3
    else:
        return 2

assert post_score('') == 0
assert post_score('SALE') == 1
assert post_score('big #sale today') == 3
assert post_score('#2024') == 3
assert post_score('hello') == 2


def read_label(text):
    if text.startswith("["):
        end = text.find("]")

        if end == -1:
            return ""
        
        return text[1:end]

    return ""


assert read_label('[HIGH] server down') == 'HIGH'
assert read_label('no tag here') == ''
assert read_label('[HIGH] it broke!') == 'HIGH'
assert read_label('[unclosed') == ''
assert read_label('Score A ]-[ Score B') == ''
assert read_label('Temperature: [HIGH]') == ''


def remove_tag(text):
    if not text.startswith("["):
        return text
    
    end = text.find("]")


    if end == -1:
            return text

    return text[end + 1:].strip()
        



assert remove_tag('[HIGH] server down') == 'server down'
assert remove_tag('no tag here') == 'no tag here'
assert remove_tag('[SKIP] ') == ''
assert remove_tag('[HIGH]     spaced out') == 'spaced out'
assert remove_tag('Temperature: [HIGH]') == 'Temperature: [HIGH]'

########################################################################

# The helper functions handle(), truncate(), tag(), priority() are already
# written for you. They are the same tools you built in Tasks 1-3.
# Call them in your own functions below; you do not need to write them.
def handle(name):
    return "@" + "".join(name.split()).lower()


def truncate(text, limit=20, suffix='...'):
    if len(text) <= limit:
        return text
    else:
        return text[:limit] + suffix


def tag(message, label='INFO'):
    return "[" + label.strip().upper() + "]" + " " + message


def priority(message):
    if message == "":
        return "skip"
    elif 'help' in message.lower() or 'down' in message.lower():
        return "high"
    elif 'are you there?' in message.lower():
        return "question"
    elif '!' in message or '?' in message:
        return "high"
    elif message.isupper():
        return "high"
    else:
        return "normal"


def clean_username(name):
    return name.strip().lower().replace(" ", "_")


def preview(name, message):
    prefix = handle(name) + ": "
    short_message = truncate(message)
    return prefix + short_message


def format_notification(name, message):
    return tag(preview(name, message), priority(message))


def read_label(line):
    if line.startswith("[") and "]" in line:
        return line[1:line.index("]")]
    else:
        return ""


def remove_tag(line):
    if line.startswith("[") and "]" in line:
        return line[line.index("]") + 1:].strip()
    else:
        return line




assert format_notification('ada lovelace',
                           'the server is completely DOWN!') == \
    '[HIGH] @adalovelace: the server is comple...'
assert format_notification('sam', 'all good') == '[NORMAL] @sam: all good'
assert format_notification('bob', 'are you there?') == \
    '[QUESTION] @bob: are you there?'
assert format_notification('sam', '') == '[SKIP] @sam: '
assert format_notification('Ada Lovelace', 'why?!') == \
    '[HIGH] @adalovelace: why?!'
