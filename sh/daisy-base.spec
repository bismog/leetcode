#BuildRoot: %{buildroot}
Summary: projectxxx base image
Name:projectxxx-base
Version: %{_version}
Release: %{_release}
Vendor: companyxxx Corporation
License: GPL
Group: Applications/Daemons
URL: http://projectxxx.companyxxx.com.cn/
Source: %{name}-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-root

Requires: docker-manage

%description
Base docker image of projectxxx

%prep

%setup -q -n  %{name}-%{version}

%build

%install
# echo $RPM_BUILD_ROOT
# rm -rf $RPM_BUILD_ROOT
# mkdir -p $RPM_BUILD_ROOT/var/lib/projectxxx/
# mkdir -p $RPM_BUILD_ROOT/usr/bin/
# cp app_tar $RPM_BUILD_ROOT/var/lib/projectxxx/
# cp -r scripts $RPM_BUILD_ROOT/var/lib/projectxxx/
# cp scripts/*sh $RPM_BUILD_ROOT/usr/bin/
## mkdir -p $RPM_BUILD_ROOT/var/lib/projectxxx-base/
## cd projectxxx-base
## install -d -m 755 %{buildroot}/var/lib/projectxxx-base
## install -p -D -m 644 projectxxx-base.tar.gz %{buildroot}/var/lib/projectxxx-base
mkdir -p $RPM_BUILD_ROOT/var/lib/projectxxx-base/
ls -l
cp projectxxx-base.tar.gz $RPM_BUILD_ROOT/var/lib/projectxxx-base/

%clean
rm -rf $RPM_BUILD_ROOT

%files

%config(noreplace) 

%defattr(0755,root,root)
/var/lib/projectxxx-base

%pre

%post
# mkdir -p /var/lib/docker-monitor/image > /dev/null 2>&1
# ln -s /var/lib/app_name/app_tar  /var/lib/docker-monitor/image/app_tar > /dev/null 2>&1
# echo "docker loading app_tar"
# docker load < /var/lib/app_name/app_tar
docker load < /var/lib/projectxxx-base/projectxxx-base.tar.gz

%preun

%changelog
