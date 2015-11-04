%global octpkg metch
# Exclude .oct files from provides
%global __provides_exclude_from ^%{octpkglibdir}/.*\\.oct$

Name:           octave-%{octpkg}
Version:        0.5.0
Release:        1%{?dist}
Summary:        Mesh/volume registration toolbox
License:        GPLv2+
URL:            http://iso2mesh.sourceforge.net/cgi-bin/index.cgi?metch
Source0:        http://downloads.sourceforge.net/iso2mesh/%{octpkg}-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  octave-devel

Requires:       octave
Requires(post): octave
Requires(postun): octave

%description
Matlab/Octave-based mesh/volume registration toolbox. It provides
straightforward functions to register point clouds (or surfaces) to a
triangular/cubic surface mesh by calculating an optimal affine transformation
(in terms of matrix A for scaling and rotation, and b for translation). It
also allows one to project a point cloud onto the surface using surface norms
and guarantee the conformity of the points to the surface. At this point, metch
can only perform rigid-body registration in terms of a linear transformation. 

%prep
%autosetup -n %{octpkg}

# Matlab only
rm -vf metchgui*.m

cat > DESCRIPTION << EOF
Name: %{octpkg}
Version: %{version}
Date: %(date +"%Y-%d-%m")
Title: %{summary}
Author: Qianqian Fang <fangq@nmr.mgh.harvard.edu>
Maintainer: Qianqian Fang <fangq@nmr.mgh.harvard.edu>
Description: Matlab/Octave-based mesh/volume registration toolbox. It provides
 straightforward functions to register point clouds (or surfaces) to a
 triangular/cubic surface mesh by calculating an optimal affine transformation
 (in terms of matrix A for scaling and rotation, and b for translation). It
 also allows one to project a point cloud onto the surface using surface norms
 and guarantee the conformity of the points to the surface. At this point, metch
 can only perform rigid-body registration in terms of a linear transformation. 
Categories: Mesh
EOF

cat > INDEX << EOF
metch >> metch
metch
 regpt2surf
 proj2mesh
 affinemap
 dist2surf
 getplanefrom3pt
 linextriangle
 nodesurfnorm
 trisurfnorm
EOF

mkdir -p inst/
mv *.m inst/

%build
%octave_pkg_build

%install
%octave_pkg_install

%post
%octave_cmd pkg rebuild

%preun
%octave_pkg_preun

%postun
%octave_cmd pkg rebuild

%files
%license COPYING
%dir %{octpkgdir}
%{octpkgdir}/*.m
%doc %{octpkgdir}/doc-cache
%{octpkgdir}/packinfo

%changelog
* Wed Nov 04 2015 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 0.5.0-1
- Initial package
