%include	/usr/lib/rpm/macros.perl
Summary:	A sophisticated backup script, based on GNU tar
Summary(pl):	Wyszukany skrypt to tworzenia kopii zapasowych
Name:		bbackup
Version:	0.52
Release:	1
License:	GPL
Group:		Networking/Utilities
Group(de):	Netzwerkwesen/Werkzeuge
Group(pl):	Sieciowe/Narzêdzia
Source0:	http://prdownloads.sourceforge.net/bbackup/%{name}-%{version}.tar.gz
Requires:	tar >= 1.12
BuildRequires:	perl >= 5.6.0
BuildRequires:	perl-AppConfig
BuildRequires:	perl-modules
BuildArch:	noarch
URL:		http://bbackup.sourceforge.net/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_sysconfdir	/etc
%define		_localstatedir	/var
%define		_libexecdir	%{_libdir}/amanda

%description 
bbackup is a sophisticated frontend for GNU-tar. It allows to perform
full backups as well as incremental backups. It can handle a number of
filesystems to be backed up (which could even be mounted at runtime).
It is possible to write backups either to streaming media or to plain
files (perferrably on a separate harddisk).

%description -l pl
bbackup jest wyszukan± nak³adk± na GNU tar. Pozwala on na tworzenie
zarówno pe³nych jak i inkrementalnych kopii zapasowych. Potrawfi
obs³ugiwaæ wiele systemów plików przeznaczonych do archiwizacji.
Mo¿liwe jest zapisywanie kopii zarówno na mediach strumieniowych jak i
w zwyk³ych plikach.

%prep
%setup -q

%install
rm -rf $RPM_BUILD_ROOT
install -d	$RPM_BUILD_ROOT{%{_bindir},%{_sysconfdir}/bbackup,%{_mandir}/man1}
ln -s		$RPM_BUILD_ROOT%{_mandir} $RPM_BUILD_ROOT/%{_prefix}/man

%{__make} install \
	BINDEST=$RPM_BUILD_ROOT%{_bindir} \
	ETCDEST=$RPM_BUILD_ROOT%{_sysconfdir} \
	MANDEST=$RPM_BUILD_ROOT%{_prefix}


gzip -9nf README THANKS TODO

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%attr(750,root,root) %dir %{_sysconfdir}/bbackup
%config(noreplace) %verify(not md5 size mtime) %attr(640,root,root) %{_sysconfdir}/bbackup/*
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man?/*
