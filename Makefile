SUBNAME = test-data
SPEC = smartmet-$(SUBNAME)
TESTDATADIRS = $(shell for i in * ; do test ! -d $$i || echo $$i ; done )

# Installation directories
ifeq ($(origin PREFIX), undefined)
  PREFIX = /usr
else
  PREFIX = $(PREFIX)
endif
datadir = $(PREFIX)/share
mydatadir = $(datadir)/smartmet
objdir = obj

# How to install
INSTALL_PROG = install -p -m 775
INSTALL_DATA = install -p -m 664

.PHONY: test rpm

# The rules
all: 
	./init_test_data

debug: all
release: all
profile: all

clean:
	rm -f *~ $(SUBNAME)/*~
	rm -rf $(objdir)
	rm -f test/*Test

install:
	@mkdir -p $(mydatadir)/test/data
	cp -r --preserve=timestamps $(TESTDATADIRS) $(mydatadir)/test/data

rpm: clean $(SPEC).spec
	rm -f $(SPEC).tar.gz # Clean a possible leftover from previous attempt
	tar -czvf $(SPEC).tar.gz --transform "s,^,$(SPEC)/," *
	rpmbuild -ta $(SPEC).tar.gz
	rm -f $(SPEC).tar.gz

# Test: checks timestamps, checks installed if installed
datatarget=$(shell test -d /usr/share/smartmet/test/data && echo /usr/share/smartmet/test/data || pwd)
test:
	test "`stat --format %y $(datatarget)/pal/200808050933_pal_skandinavia_pinta.sqd`" = "2008-08-05 06:31:00.000000000 +0000"
	test "`stat --format %y $(datatarget)/pal/200808050729_pal_skandinavia_pinta.sqd`" = "2008-08-05 04:27:00.000000000 +0000"
	test "`stat --format %y $(datatarget)/harmonie/201705110343_harmonie_hybrid-cropped.sqd`" = "2017-05-11 00:00:00.000000000 +0000"
	test "`stat --format %y $(datatarget)/hirlam/201303180352_hirlam_eurooppa_pinta_cropped.sqd`" = "2013-03-18 00:00:00.000000000 +0000"
	@echo "File timestamp tests passed ok"
