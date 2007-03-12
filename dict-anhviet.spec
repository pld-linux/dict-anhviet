%define		dictname anhviet
Summary:	English-Vietnamese dictionary for dictd
Summary(pl.UTF-8):	Słownik angielsko-wietnamski dla dictd
Name:		dict-%{dictname}
Version:	1.0
Release:	4
License:	GPL (?)
Group:		Applications/Dictionaries
Source0:	http://vietlug.sourceforge.net/download/emacs/%{dictname}.index
# Source0-md5:	f319c97dd99a8890f27d947b23820e8f
Source1:	http://vietlug.sourceforge.net/download/emacs/%{dictname}.utf.dz
# Source1-md5:	e96b030c7814d8ee9dbd30cd039e5f70
URL:		http://vietlug.sourceforge.net/
BuildRequires:	rpmbuild(macros) >= 1.268
Requires:	%{_sysconfdir}/dictd
Requires:	dictd
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
English-Vietnamese dictionary for dictd.

%description -l pl.UTF-8
Słownik angielsko-wietnamski dla dictd.

%prep

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_datadir}/dictd,%{_sysconfdir}/dictd}

install %{SOURCE0} $RPM_BUILD_ROOT%{_datadir}/dictd
install %{SOURCE1} $RPM_BUILD_ROOT%{_datadir}/dictd/%{dictname}.dict.dz

dictprefix=%{_datadir}/dictd/%{dictname}
echo "# English-Vietnamese dictionary
database %{dictname} {
	data  \"$dictprefix.dict.dz\"
	index \"$dictprefix.index\"
}" > $RPM_BUILD_ROOT%{_sysconfdir}/dictd/%{dictname}.dictconf

%clean
rm -rf $RPM_BUILD_ROOT

%post
%service -q dictd restart

%postun
if [ "$1" = 0 ]; then
	%service -q dictd restart
fi

%files
%defattr(644,root,root,755)
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/dictd/%{dictname}.dictconf
%{_datadir}/dictd/%{dictname}.*
