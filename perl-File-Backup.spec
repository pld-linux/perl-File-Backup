%include	/usr/lib/rpm/macros.perl
%define	pdir	File
%define	pnam	Backup
Summary:	File::Backup perl module
Summary(pl):	Modu³ perla File::Backup
Name:		perl-File-Backup
Version:	0.0602
Release:	1
License:	GPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	c193d20e55635ea63d402b93ebe2a2f0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	perl-devel >= 5.6
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
File::Backup - For making rotating backups of directories.

%description -l pl
File::Backup umo¿liwia rotacjê archiwów.

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
%{perl_vendorlib}/%{pdir}/%{pnam}.pm
%{_mandir}/man3/*
