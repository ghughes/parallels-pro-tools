import re, os, socket
from vh3 import virthost
from vh3.modules import imap

for site in virthost.get_domain_list():
    config, errs = virthost.get_configs_from_site(site)
    domain = config['siteinfo']['domain']
    
    mx = []
    
    f = os.popen("nslookup -q=mx %s" % domain)
    for i in f.readlines():
        m = re.search(r'mail exchanger = \d+ (\S+).\s', i)
        if m:
            mx.append(m.group(1))
    
    print config['siteinfo']['domain']
    
    mailboxes = imap.get_enabled_users(site)
    if len(mailboxes) > 0:
        print 'Mailboxes:', ', '.join(mailboxes)
        
    aliases = []
    f = open('/home/virtual/%s/fst/etc/aliases' % site, 'r')
    for i in f.readlines():
        m = re.search(r'([^:]+):\s+([^\s,]+)', i)
        if m:
            frm = m.group(1)
            to = m.group(2)
            
            if frm == 'MAILER-DAEMON' or frm == 'postmaster' or frm == 'site_blackhole' or frm == 'majordomo' or frm == 'root':
                continue
            
            aliases.append('%s -> %s' % (frm, to))
            
    if len(aliases) > 0:
        print 'Aliases:', ', '.join(aliases)
    
    if len(mx) > 0:
        print 'Servers:', ', '.join(mx), '\n'
    else:
        print
