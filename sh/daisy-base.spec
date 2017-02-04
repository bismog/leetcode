#BuildRoot: %{buildroot}
Summary: daisy base image
Name:daisy-base
Version: %{_version}
Release: %{_release}
Vendor: ZTE Corporation
License: GPL
Group: Applications/Daemons
URL: http://daisy.zte.com.cn/
Source: %{name}-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-root

Requires: docker-manage

%description
Base docker image of daisy

%prep

%setup -q -n  %{name}-%{version}

%build

%install
# echo $RPM_BUILD_ROOT
# rm -rf $RPM_BUILD_ROOT
# mkdir -p $RPM_BUILD_ROOT/var/lib/daisy/
# mkdir -p $RPM_BUILD_ROOT/usr/bin/
# cp app_tar $RPM_BUILD_ROOT/var/lib/daisy/
# cp -r scripts $RPM_BUILD_ROOT/var/lib/daisy/
# cp scripts/*sh $RPM_BUILD_ROOT/usr/bin/
## mkdir -p $RPM_BUILD_ROOT/var/lib/daisy-base/
## cd daisy-base
## install -d -m 755 %{buildroot}/var/lib/daisy-base
## install -p -D -m 644 daisy-base.tar.gz %{buildroot}/var/lib/daisy-base
mkdir -p $RPM_BUILD_ROOT/var/lib/daisy-base/
ls -l
cp daisy-base.tar.gz $RPM_BUILD_ROOT/var/lib/daisy-base/

%clean
rm -rf $RPM_BUILD_ROOT

%files

%config(noreplace) 

%defattr(0755,root,root)
/var/lib/daisy-base

%pre

%post
# mkdir -p /var/lib/docker-monitor/image > /dev/null 2>&1
# ln -s /var/lib/app_name/app_tar  /var/lib/docker-monitor/image/app_tar > /dev/null 2>&1
# echo "docker loading app_tar"
# docker load < /var/lib/app_name/app_tar
docker load < /var/lib/daisy-base/daisy-base.tar.gz

%preun

%changelog
