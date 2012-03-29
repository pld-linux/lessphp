Summary:	lessphp is a compiler for LESS written in PHP
Name:		lessphp
Version:	0.3.3
Release:	1
License:	MIT/GPL v3
Group:		Applications
Source0:	http://leafo.net/lessphp/src/%{name}-%{version}.tar.gz
# Source0-md5:	7a228e3239c5bf8dce7435447c3bb234
#Source0:	https://github.com/leafo/lessphp/tarball/master#/%{name}.tgz
Patch0:		fixes.patch
URL:		http://leafo.net/lessphp/
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
lessphp is a compiler that generates CSS from a small superset
language that adds many additional features seen in other languages.
It is based off an original Ruby implementation called LESS.

%prep
%setup -qc
mv *%{name}*/* .
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
