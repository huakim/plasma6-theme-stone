Name: plasma6-theme-stone
Version: 0
Release: 0
Summary: A Kde Plasma theme
License: GPLv2
Url: https://github.com/ddh4r4m/Stone
BuildRequires: kf6-filesystem
Requires: tela-icon-theme
Recommends: stone-wallpapers
Provides: plasma-theme-stone
Requires: stone-colorschemes
Source: %{name}-%{version}.tar.gz

%description
%{summary}.

%prep
%autosetup

%install
mkdir -pv %{buildroot}%{_datadir}
mkdir -pv %{buildroot}%{_kf6_plasmadir}
cp -Rfv plasma/look-and-feel %{buildroot}%{_kf6_plasmadir}/
cp -Rfv plasma/desktoptheme %{buildroot}%{_kf6_plasmadir}/
cp -Rfv wallpapers %{buildroot}%{_datadir}/
cp -Rfv color-schemes %{buildroot}%{_datadir}/
cp -Rfv konsole %{buildroot}%{_datadir}/


%package -n stone-colorschemes
Summary: %{summary}
%description -n stone-colorschemes
%{summary}.
%package -n stone-wallpapers
Summary: %{summary}
%description -n stone-wallpapers
%{summary}.
%package -n konsole-stone-theme
Summary: %{summary}
%description -n konsole-stone-theme
%{summary}.


%files
%{_kf6_plasmadir}/look-and-feel/Stone
%{_kf6_plasmadir}/desktoptheme/Stone

%files -n stone-colorschemes
%{_datadir}/color-schemes/Stone.colors

%files -n stone-wallpapers
%{_datadir}/wallpapers/Stone

%files -n konsole-stone-theme
%{_datadir}/konsole/*
