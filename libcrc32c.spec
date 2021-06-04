#
# spec file for package libcrc32c
#

%define packagename crc32c
%define soname 1
Name:           libcrc32c
Version:        1.1.1
Release:        0
Summary:        CRC32C implementation with support for CPU-specific acceleration instructions
License:        BSD-3-Clause
Group:          Development/Libraries/C and C++
URL:            https://github.com/google/crc32c
Source0:        %{packagename}-%{version}.tar.gz
BuildRequires:  cmake
BuildRequires:  gcc-c++

%description
This project collects a few CRC32C implementations under an umbrella 
that dispatches to a suitable implementation based on the host computer's 
hardware capabilities.

CRC32C is specified as the CRC that uses the iSCSI polynomial in RFC 3720. 
The polynomial was introduced by G. Castagnoli, S. Braeuer and M. Herrmann.

%package -n %{name}%{soname}
Summary:        CRC32C implementation with support for CPU-specific acceleration instructions
Group:          System/Libraries

%description -n %{name}%{soname}
This project collects a few CRC32C implementations under an umbrella 
that dispatches to a suitable implementation based on the host computer's 
hardware capabilities.

CRC32C is specified as the CRC that uses the iSCSI polynomial in RFC 3720. 
The polynomial was introduced by G. Castagnoli, S. Braeuer and M. Herrmann.

%package -n %{name}-devel
Summary:        C++ header files and library symbolic links for %{packagename}
Group:          Development/Libraries/C and C++
Requires:       %{name}%{soname} = %{version}

%description -n %{name}-devel
This package contains the C++ header files and symbolic links to the shared
libraries for %{name}. If you would like to develop programs using %{name},
you will need to install %{name}-devel.

%prep
%setup -q -n %{packagename}-%{version}

%build
cmake -DCMAKE_INSTALL_PREFIX=/usr -DCRC32C_BUILD_TESTS=0 -DCRC32C_BUILD_BENCHMARKS=0 -DCRC32C_USE_GLOG=0 -DBUILD_SHARED_LIBS=1
make all

%install
%make_install DESTDIR=%{buildroot} includedir=%{_includedir} libdir=%{_libdir}

%post -n %{name}%{soname} -p /sbin/ldconfig
%postun -n %{name}%{soname} -p /sbin/ldconfig

%files -n %{name}%{soname}
%license LICENSE
%doc AUTHORS CONTRIBUTING.md README.md
%{_libdir}/%{name}.so.1.1.0
%{_libdir}/%{name}.so.1

%files -n %{name}-devel
%{_includedir}/%{packagename}
%{_libdir}/%{name}.so
%{_libdir}/cmake/Crc32c

%changelog

