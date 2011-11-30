all:
	@echo "Prepping for RPM build...";
	@mkdir -p /var/tmp/Rhipe-0.66-1-root/RPMS/x86_64
	@mkdir -p /var/tmp/Rhipe-0.66-1-root/SRPMS
	@mkdir -p /var/tmp/Rhipe-0.66-1-root/BUILD/usr/lib64/R/library
	@cp -r SPECS /var/tmp/Rhipe-0.66-1-root/SPECS
	@cp -r SOURCES /var/tmp/Rhipe-0.66-1-root/
	@echo "Generating the RPM...";
	@rpmbuild -bb /var/tmp/Rhipe-0.66-1-root/SPECS/RHIPE-RPM.spec
	@mkdir artifacts
	@cp /var/tmp/Rhipe-0.66-1-root/RPMS/x86_64/*.rpm artifacts
	@echo "Done";

clean:
	@rm -rf /var/tmp/Rhipe-0.66-1-root
	@rm -rf ./artifacts
	@rm -rf SPECS/*~
	@rm -rf ./*~
	echo "All Clean!";
