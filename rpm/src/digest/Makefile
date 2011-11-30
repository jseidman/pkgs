all:
	@echo "Prepping for RPM build...";
	@mkdir -p /var/tmp/digest-0.5.1-1-root/RPMS/x86_64
	@mkdir -p /var/tmp/digest-0.5.1-1-root/SRPMS
	@mkdir -p /var/tmp/digest-0.5.1-1-root/BUILD/usr/lib64/R/library
	@cp -r SPECS /var/tmp/digest-0.5.1-1-root/SPECS
	@cp -r SOURCES /var/tmp/digest-0.5.1-1-root/
	@echo "Generating the RPM...";
	@rpmbuild -bb /var/tmp/digest-0.5.1-1-root/SPECS/digest-0.5.1.spec
	@mkdir artifacts
	@cp /var/tmp/digest-0.5.1-1-root/RPMS/x86_64/*.rpm artifacts
	@echo "Done";

clean:
	@rm -rf /var/tmp/digest-0.5.1-1-root
	@rm -rf ./artifacts
	@rm -rf SPECS/*~
	@rm -rf ./*~
	echo "All Clean!";
