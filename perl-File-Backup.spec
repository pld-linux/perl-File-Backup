%include	/usr/lib/rpm/macros.perl
Summary:	File-Backup perl module
Summary(pl):	Modu³ perla File-Backup
Name:		perl-File-Backup
Version:	0.02
Release:	5
License:	GPL
Group:		Development/Languages/Perl
Group(de):	Entwicklung/Sprachen/Perl
Group(pl):	Programowanie/Jêzyki/Perl
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/File/File-Backup-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.6
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
File-Backup - For making rotating backups of directories.

%description -l pl
File-Backup umo¿liwia rotacjê archiwów.

%prep
%setup -q -n File-Backup-%{version}

%build
perl Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%{perl_sitelib}/File/Backup.pm
%{_mandir}/man3/*
