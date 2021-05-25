#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-Exporter-Declare
Version  : 0.114
Release  : 17
URL      : https://cpan.metacpan.org/authors/id/E/EX/EXODIST/Exporter-Declare-0.114.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/E/EX/EXODIST/Exporter-Declare-0.114.tar.gz
Summary  : 'Exporting done right'
Group    : Development/Tools
License  : Artistic-1.0-Perl
Requires: perl-Exporter-Declare-perl = %{version}-%{release}
BuildRequires : buildreq-cpan
BuildRequires : perl(Fennec::Lite)
BuildRequires : perl(Meta::Builder)
BuildRequires : perl(Test::Exception)
BuildRequires : perl(aliased)

%description
NAME
Exporter::Declare - Exporting done right
DESCRIPTION
Exporter::Declare is a meta-driven exporting tool. Exporter::Declare
tries to adopt all the good features of other exporting tools, while
throwing away horrible interfaces. Exporter::Declare also provides
hooks that allow you to add options and arguments for import. Finally,
Exporter::Declare's meta-driven system allows for top-notch
introspection.

%package dev
Summary: dev components for the perl-Exporter-Declare package.
Group: Development
Provides: perl-Exporter-Declare-devel = %{version}-%{release}
Requires: perl-Exporter-Declare = %{version}-%{release}

%description dev
dev components for the perl-Exporter-Declare package.


%package perl
Summary: perl components for the perl-Exporter-Declare package.
Group: Default
Requires: perl-Exporter-Declare = %{version}-%{release}

%description perl
perl components for the perl-Exporter-Declare package.


%prep
%setup -q -n Exporter-Declare-0.114
cd %{_builddir}/Exporter-Declare-0.114

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%install
rm -rf %{buildroot}
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/Exporter::Declare.3
/usr/share/man/man3/Exporter::Declare::Export.3
/usr/share/man/man3/Exporter::Declare::Export::Alias.3
/usr/share/man/man3/Exporter::Declare::Export::Generator.3
/usr/share/man/man3/Exporter::Declare::Export::Sub.3
/usr/share/man/man3/Exporter::Declare::Export::Variable.3
/usr/share/man/man3/Exporter::Declare::Meta.3
/usr/share/man/man3/Exporter::Declare::Specs.3

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.34.0/Exporter/Declare.pm
/usr/lib/perl5/vendor_perl/5.34.0/Exporter/Declare/Export.pm
/usr/lib/perl5/vendor_perl/5.34.0/Exporter/Declare/Export/Alias.pm
/usr/lib/perl5/vendor_perl/5.34.0/Exporter/Declare/Export/Generator.pm
/usr/lib/perl5/vendor_perl/5.34.0/Exporter/Declare/Export/Sub.pm
/usr/lib/perl5/vendor_perl/5.34.0/Exporter/Declare/Export/Variable.pm
/usr/lib/perl5/vendor_perl/5.34.0/Exporter/Declare/Meta.pm
/usr/lib/perl5/vendor_perl/5.34.0/Exporter/Declare/Specs.pm
