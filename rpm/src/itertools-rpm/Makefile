all:
	@echo "Prepping for RPM build...";
	@mkdir -p /var/tmp/itertools-0.1-1-root/RPMS/x86_64
	@mkdir -p /var/tmp/itertools-0.1-1-root/SRPMS
	@mkdir -p /var/tmp/itertools-0.1-1-root/BUILD/usr/lib64/R/library
	@cp -r SPECS /var/tmp/itertools-0.1-1-root/SPECS
	@cp -r SOURCES /var/tmp/itertools-0.1-1-root/
	@echo "Generating the RPM...";
	@rpmbuild -bb /var/tmp/itertools-0.1-1-root/SPECS/itertools-0.1.spec
	@mkdir artifacts
	@cp /var/tmp/itertools-0.1-1-root/RPMS/x86_64/*.rpm artifacts
	@echo "Done";

clean:
	@rm -rf /var/tmp/itertools-0.1-1-root
	@rm -rf ./artifacts
	@rm -rf SPECS/*~
	@rm -rf ./*~
	echo "All Clean!";
