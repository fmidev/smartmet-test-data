SUBNAME = test-data
SPEC = smartmet-$(SUBNAME)
TESTDATADIRS = $(shell for i in * ; do test ! -d $$i || echo $$i ; done )

# Installation directories
processor := $(shell uname -p)

ifeq ($(origin PREFIX), undefined)
  PREFIX = /usr
else
  PREFIX = $(PREFIX)
endif

ifeq ($(processor), x86_64)
  libdir = $(PREFIX)/lib64
else
  libdir = $(PREFIX)/lib
endif

bindir = $(PREFIX)/bin
includedir = $(PREFIX)/include
datadir = $(PREFIX)/share
mydatadir = $(datadir)/smartmet
objdir = obj



# How to install
INSTALL_PROG = install -p -m 775
INSTALL_DATA = install -p -m 664

.PHONY: test rpm

# The rules

all: 
debug: all
release: all
profile: all

clean:
	rm -f *~ $(SUBNAME)/*~
	rm -rf $(objdir)
	rm -f test/*Test

format:
	clang-format -i -style=file $(SUBNAME)/*.h $(SUBNAME)/*.cpp test/*.cpp

install:
	@mkdir -p $(mydatadir)/test/data
	$(INSTALL_PROG) init_test_data $(mydatadir)/test
	@mkdir -p $(bindir)
	ln -srf $(mydatadir)/test/init_test_data $(bindir)/init_test_data
	cp -r $(TESTDATADIRS) $(mydatadir)/test/data

test:
	@echo Nothing to be done here.

rpm: clean $(SPEC).spec
	rm -f $(SPEC).tar.gz # Clean a possible leftover from previous attempt
	tar -czvf $(SPEC).tar.gz --transform "s,^,$(SPEC)/," *
	rpmbuild -ta $(SPEC).tar.gz
	rm -f $(SPEC).tar.gz
