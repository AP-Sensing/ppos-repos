BuildArch:     noarch
Name:          ppos-repos
Version:       38
Release:       4
License:       GPLv3
Group:         Unspecified
Summary:       AP Sesning RPM repositories for PhotonPonyOS
Distribution:  PhotonPonyOS

URL:           https://github.com/AP-Sensing/ppos-repos/tree/ppos38
Vendor:        AP Sensing
Packager:      AP Sensing
Provides:      ppos-repos = %{version}-%{release}
Requires:      system-release(%{version})

Source1: ppos.repo
Source2: RPM-GPG-KEY-ppos-primary


%description
This package provides AP Sensing RPM (dnf, yum and rpm-ostree) repository configurations for PhotonPonyOS.

%prep

%build

%install
# Install GPG keys
install -d -m 755 $RPM_BUILD_ROOT/etc/pki/rpm-gpg
install -m 644 %{_sourcedir}/RPM-GPG-KEY-ppos-primary $RPM_BUILD_ROOT/etc/pki/rpm-gpg/

pushd $RPM_BUILD_ROOT/etc/pki/rpm-gpg/
ln -s RPM-GPG-KEY-ppos-primary RPM-GPG-KEY-ppos-38-primary
popd

# Install repo files
install -d -m 755 $RPM_BUILD_ROOT/etc/yum.repos.d
install -m 644 %{_sourcedir}/ppos.repo $RPM_BUILD_ROOT/etc/yum.repos.d

%files
%dir /etc/yum.repos.d
%config(noreplace) /etc/yum.repos.d/ppos.repo

%dir /etc/pki/rpm-gpg
/etc/pki/rpm-gpg/RPM-GPG-KEY-*

%changelog
* Fri Jun 09 2023 Fabian Sauter <fabian.sauter+rpm@apsensing.com> - 38-1
- Initial release
* Thu Jun 15 2023 Fabian Sauter <fabian.sauter+rpm@apsensing.com> - 38-4
- Using https for the repos