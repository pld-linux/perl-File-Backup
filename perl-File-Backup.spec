#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	File
%define	pnam	Backup
Summary:	File::Backup - easy file backup & rotation automation
Summary(pl):	File::Backup - ³atwa archiwizacja i rotacja plików
Name:		perl-File-Backup
Version:	0.07
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	f53d6a22587abfde366ea84c141b716b
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	perl-devel >= 1:5.8.0
%if %{with tests}
BuildRequires:	perl-File-Which
BuildRequires:	perl-LockFile-Simple
%endif
Requires:	gzip
Requires:	tar
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The File::Backup legacy Perl module implements archival and
compression (A.K.A "backup") and file rotation and is an
implementation of "tar" and "gzip" calls.

%description -l pl
Modu³ Perla File::Backup stanowi implementacjê archiwizacji i
kompresji ("backup") oraz rotacjê archiwów i jest zaimplementowany
poprzez wywo³ania programów tar i gzip.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%{perl_vendorlib}/%{pdir}/%{pnam}.pm
%{_mandir}/man3/*
