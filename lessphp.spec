%define		php_min_version 5.1.0
%include	/usr/lib/rpm/macros.php
Summary:	lessphp is a compiler for LESS written in PHP
Name:		lessphp
Version:	0.5.0
Release:	2
License:	MIT/GPL v3
Group:		Applications
Source0:	https://github.com/leafo/lessphp/archive/v%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	85fc1d7734e4e146566681418c69ead6
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
%setup -q
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
