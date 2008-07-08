Summary:	SkyEye - an Open Source Simulator for ARM
Summary(pl.UTF-8):	SkyEye - symulator procesora ARM
Name:		skyeye
Version:	1.2.5
Release:	1
License:	GPL v2+
Group:		Applications
Source0:	http://download.gro.clinux.org/skyeye/%{name}-%{version}_REL.tar.gz
# Source0-md5:	afa9b84961e17b306b656df143775292
Source1:	skyeye.conf
URL:		http://www.skyeye.org/
BuildRequires:	gtk+2-devel >= 2.0.0
BuildRequires:	pkgconfig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
SkyEye is an Open Source Simulator, which can simulate Atmel AT91,
EP7312, cs89712, StrongARM (SA1100/SA1110), XScale PXA25x. Users can
run Operating Systems such as Linux, uCLinux, uC/OS-II for ARM and can
analyze or debug in source level.

%description -l pl.UTF-8
SkyEye jest symulatorem o otwartych źródłach. Symuluje następujące 
procesory: Atmel AT91, EP7312, cs89712, StrongARM (SA1100/SA1110), 
XScale PXA25x. Umożliwia uruchomienie systemów operacyjnych
takich jak Linux, uCLinux, uC/OS-II na procesorze ARM, ich
analizę i odpluskiwanie na poziomie kodu źródłowego.

%prep
%setup -qn %{name}-%{version}_REL
install %{SOURCE1} .

%build
%{__aclocal}
%{__automake}
%{__autoconf}

%configure	\
	--enable-lcd

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install	\
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog README skyeye.conf
%attr(755,root,root) %{_bindir}/skyeye
