%include	/usr/lib/rpm/macros.perl
%define	pdir	File
%define	pnam	Backup
Summary:	File::Backup perl module
Summary(pl):	Modu� perla File::Backup
Name:		perl-File-Backup
Version:	0.02
Release:	9
License:	GPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	eab684da395c1df7c5275d0c0c911b95
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	perl-devel >= 5.6
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
File::Backup - For making rotating backups of directories.

%description -l pl
File::Backup umo�liwia rotacj� archiw�w.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%{perl_vendorlib}/File/Backup.pm
%{_mandir}/man3/*
