Summary:	A sophisticated backup script, based on GNU tar
Summary(pl.UTF-8):	Wyszukany skrypt to tworzenia kopii zapasowych
Name:		bbackup
Version:	0.52
Release:	3
License:	GPL
Group:		Networking/Utilities
Source0:	http://dl.sourceforge.net/bbackup/%{name}-%{version}.tar.gz
# Source0-md5:	3fcff65424da518ca351971c00b51912
URL:		http://bbackup.sourceforge.net/
BuildRequires:	perl-AppConfig
BuildRequires:	perl-devel >= 1:5.6.0
BuildRequires:	perl-perldoc
BuildRequires:	rpm-perlprov
Requires:	tar >= 1.12
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
bbackup is a sophisticated frontend for GNU-tar. It allows you to
perform full backups as well as incremental backups. It can handle a
number of filesystems to be backed up (which could even be mounted at
runtime). It is possible to write backups either to streaming media or
to plain files (preferably on a separate harddisk).

%description -l pl.UTF-8
bbackup jest wyrafinowaną nakładką na GNU tar. Pozwala on na tworzenie
zarówno pełnych jak i inkrementalnych kopii zapasowych. Potrafi
obsługiwać wiele systemów plików przeznaczonych do archiwizacji.
Możliwe jest zapisywanie kopii zarówno na mediach strumieniowych jak i
w zwykłych plikach.

%prep
%setup -q

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_sysconfdir}/bbackup,%{_mandir}/man1} \
	$RPM_BUILD_ROOT%{_var}/bbackup

%{__make} install \
	BINDEST=$RPM_BUILD_ROOT%{_bindir} \
	ETCDEST=$RPM_BUILD_ROOT%{_sysconfdir} \
	MANDEST=$RPM_BUILD_ROOT%{_datadir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README THANKS TODO
%attr(750,root,root) %dir %{_var}/bbackup
%attr(750,root,root) %dir %{_sysconfdir}/bbackup
%config(noreplace) %verify(not md5 mtime size) %attr(640,root,root) %{_sysconfdir}/bbackup/*
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man?/*
