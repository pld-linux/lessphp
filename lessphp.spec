%define		php_min_version 5.1.0
Summary:	lessphp is a compiler for LESS written in PHP
Name:		lessphp
Version:	0.5.1
Release:	1
License:	MIT/GPL v3
Group:		Applications
Source0:	https://github.com/marcusschwarz/lesserphp/archive/v%{version}/lesserphp-%{version}.tar.gz
# Source0-md5:	d10869d75c1468b0e918a538f58076f1
Patch0:		fixes.patch
URL:		http://leafo.net/lessphp/
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
Requires:	/usr/bin/php
Requires:	php(core) >= %{php_min_version}
Requires:	php(ctype)
Requires:	php(date)
Requires:	php(pcre)
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
lessphp is a compiler that generates CSS from a small superset
language that adds many additional features seen in other languages.
It is based off an original Ruby implementation called LESS.

%prep
%setup -q -n lesserphp-%{version}
%patch0 -p1

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{php_data_dir}}
install -p plessc $RPM_BUILD_ROOT%{_bindir}
cp -p lessc.inc.php $RPM_BUILD_ROOT%{php_data_dir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc LICENSE README.md
%attr(755,root,root) %{_bindir}/plessc
%{php_data_dir}/lessc.inc.php
