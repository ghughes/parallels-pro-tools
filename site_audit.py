from vh3 import virthost

print 'Site,Enabled,UsedBandwidth,MaxBandwidth,Webalizer,Awstats,Emails,Backup,Databases'

for site in virthost.get_domain_list():
	config, errs = virthost.get_configs_from_site(site)
	usage, errs = virthost.get_site_usage(site)
	print '%s,%s,%s,%s,%s,%s,%s,%s,%s' % (
		config['siteinfo']['domain'],
		config['siteinfo']['enabled'],
		long(usage['bandwidth']['usage']) / 1048576,
		long(config['bandwidth']['threshold']) / 1048576,
		config['webalizer']['enabled'],
		config['awstats']['enabled'],
		usage['users']['usage'],
		config['vhbackup']['enabled'],
		usage['mysql']['usage'])		
