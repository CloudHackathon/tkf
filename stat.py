from pprint import pprint
ups = ['SH603036', 'SH600239', 'SH603990', 'SH600173', 'SH600909', 'SH601882', 'SH600466', 'SH603819', 'SH601116', 'SH603033']
downs = ["SH603025", "SH603159", "SH603900", "SH603987", "SH603977", "SH603060", "SH603323", "SH600848", "SH603999", "SH603727"]
def calc(f):
    lines = open('samples/'+f).read().split('\n')
    cats = {'user.time': 0, 'user.reply': 0, 'all.time': 0, 'all.alpha': 0}
    for line in lines:
        res = line.split(' ')
        
        if len(res) < 4: continue
        score = float(res[2])
        t = res[0]
        cats[t] += score - 0.5

    return cats

cats = {'user.time': [], 'user.reply': [], 'all.time': [], 'all.alpha': []}
keys = ['user.time', 'user.reply', 'all.time', 'all.alpha']
print '\nups\n'
for f in ups:
    cat = calc(f)
    for k in keys:
        cats[k].append(float('%.2f' % cat[k]))

for k in keys:
    print k, cats[k]

cats = {'user.time': [], 'user.reply': [], 'all.time': [], 'all.alpha': []}
print '\ndowns\n'
for f in downs:
    cat = calc(f)
    for k in keys:
        cats[k].append(float('%.2f' % cat[k]))

for k in keys:
    print k, cats[k]
