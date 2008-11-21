%define pdfdir http://media.texample.net/tikz/examples/PDF
%define texdir http://media.texample.net/tikz/examples/TEX
Summary:	TikZ examples
Summary(hu.UTF-8):	TikZ példák
Name:		tetex-latex-tikz-examples
Version:	20081120
Release:	1.1
License:	LaTeX Project Public License
Group:		Applications/Publishing/TeX
URL:		http://www.texample.net/tikz/examples/
# chemistry
Source0:	%{pdfdir}/atoms-and-orbitals.pdf
Source1:	%{texdir}/atoms-and-orbitals.tex
Source2:	%{pdfdir}/oxidation-and-reduction.pdf
Source3:	%{texdir}/oxidation-and-reduction.tex
# computer
Source4:	%{pdfdir}/actor-transaction-diagram.pdf
Source5:	%{texdir}/actor-transaction-diagram.tex
Source6:	%{pdfdir}/computer-science-mindmap.pdf
Source7:	%{texdir}/computer-science-mindmap.tex
Source8:	%{pdfdir}/distributed-processing.pdf
Source9:	%{texdir}/distributed-processing.tex
Source10:	%{pdfdir}/interaction-nets.pdf
Source11:	%{texdir}/interaction-nets.tex
Source12:	%{pdfdir}/manet.pdf
Source13:	%{texdir}/manet.tex
Source14:	%{pdfdir}/prims-algorithm.pdf
Source15:	%{texdir}/prims-algorithm.tex
Source16:	%{pdfdir}/star-graph.pdf
Source17:	%{texdir}/star-graph.tex
Source18:	%{pdfdir}/timing-diagram.pdf
Source19:	%{texdir}/timing-diagram.tex
Source20:	%{pdfdir}/pgf-umlsd.pdf
Source21:	%{texdir}/pgf-umlsd.tex
# electrical
Source22:	%{pdfdir}/circuitikz.pdf
Source23:	%{texdir}/circuitikz.tex
Source24:	%{pdfdir}/control-system-principles.pdf
Source25:	%{texdir}/control-system-principles.tex
Source26:	%{pdfdir}/circuit-decorations.pdf
Source27:	%{texdir}/circuit-decorations.tex
Source28:	%{pdfdir}/FIR-filter.pdf
Source29:	%{texdir}/FIR-filter.tex
Source30:	%{pdfdir}/logic-circuits-library.pdf
Source31:	%{texdir}/logic-circuits-library.tex
Source32:	%{pdfdir}/radix2fft.pdf
Source33:	%{texdir}/radix2fft.tex
Source34:	%{pdfdir}/schemabloc.pdf
Source35:	%{texdir}/schemabloc.tex
Source36:	%{pdfdir}/signal-flow-building-blocks.pdf
Source37:	%{texdir}/signal-flow-building-blocks.tex
Source38:	%{pdfdir}/simple-circuit-schematics-symbols.pdf
Source39:	%{texdir}/simple-circuit-schematics-symbols.tex
# mathematics
Source40:	%{pdfdir}/animated-set-intersection.pdf
Source41:	%{texdir}/animated-set-intersection.tex
Source42:	%{pdfdir}/tutorial.pdf
Source43:	%{texdir}/tutorial.tex
Source44:	%{pdfdir}/hilbert-curve.pdf
Source45:	%{texdir}/hilbert-curve.tex
Source46:	%{pdfdir}/parallel-lines.pdf
Source47:	%{texdir}/parallel-lines.tex
Source48:	%{pdfdir}/polygon-division.pdf
Source49:	%{texdir}/polygon-division.tex
Source50:	%{pdfdir}/sign-diagram.pdf
Source51:	%{texdir}/sign-diagram.tex
Source52:	%{pdfdir}/star-graph.pdf
Source53:	%{texdir}/star-graph.tex
# physics
Source54:	%{pdfdir}/beamer-arrows.pdf
Source55:	%{texdir}/beamer-arrows.tex
Source56:	%{pdfdir}/feynman-diagram.pdf
Source57:	%{texdir}/feynman-diagram.tex
Source58:	%{pdfdir}/free-body-diagrams.pdf
Source59:	%{texdir}/free-body-diagrams.tex
Source60:	%{pdfdir}/gamma-interaction.pdf
Source61:	%{texdir}/gamma-interaction.tex
Source62:	%{pdfdir}/global-nodes.pdf
Source63:	%{texdir}/global-nodes.tex
Source64:	%{pdfdir}/oblique-incidence.pdf
Source65:	%{texdir}/oblique-incidence.tex
# statistics
Source66:	%{pdfdir}/animated-distributions.pdf
Source67:	%{texdir}/animated-distributions.tex
Source68:	%{pdfdir}/box-and-whisker-plot.pdf
Source69:	%{texdir}/box-and-whisker-plot.tex
Source70:	%{pdfdir}/standard-deviation.pdf
Source71:	%{texdir}/standard-deviation.tex
Requires:	tetex-latex
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define _exampledir %{_datadir}/texmf/doc/latex/tikz/examples

%description
TikZ examples.

%description -l hu.UTF-8
TikZ példák.


%package chemistry
Summary:	TikZ chemistry examples
Summary(hu.UTF-8):	TikZ kémiai példák
Group:		Applications/Publishing/TeX

%description chemistry
TikZ chemistry examples

%description chemistry -l hu.UTF-8
TikZ kémiai példák


%package computer
Summary:	TikZ computer science examples
Summary(hu.UTF-8):	TikZ számítógép-tudományi példák
Group:		Applications/Publishing/TeX

%description computer
TikZ computer science examples

%description computer -l hu.UTF-8
TikZ számítógép-tudományi példák


%package electrical
Summary:	TikZ electrical engineering examples
Summary(hu.UTF-8):	TikZ elektronikai példák
Group:		Applications/Publishing/TeX
# need to compile
Suggests:	tetex-latex-circuitikz
Suggests:	tetex-tex-xkeyval

%description electrical
TikZ electrical engineering examples

%description electrical -l hu.UTF-8
TikZ elektronikai példák


%package mathematics
Summary:	TikZ mathematics examples
Summary(hu.UTF-8):	TikZ matematikai példák
Group:		Applications/Publishing/TeX

%description mathematics
TikZ mathematics examples

%description mathematics -l hu.UTF-8
TikZ matematikai példák


%package physics
Summary:	TikZ physics examples
Summary(hu.UTF-8):	TikZ fizikai példák
Group:		Applications/Publishing/TeX

%description physics
TikZ physics examples

%description physics -l hu.UTF-8
TikZ fizikai példák


%package statistics
Summary:	TikZ statistics examples
Summary(hu.UTF-8):	TikZ statisztikai példák
Group:		Applications/Publishing/TeX

%description statistics
TikZ statistics examples

%description statistics -l hu.UTF-8
TikZ statisztikai példák


%prep
# empty

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_exampledir}
( cat << EOF
TeXample.net is a web site dedicated to the wonderful world of TeX and friends.
The site is still under heavily construction, so sorry for all the mess.
Content, features and design will be added gradually.
EOF
) > $RPM_BUILD_ROOT%{_exampledir}/README

# chemistry
install -d $RPM_BUILD_ROOT%{_exampledir}/chemistry
install %{SOURCE0} %{SOURCE1} %{SOURCE2} %{SOURCE3} $RPM_BUILD_ROOT%{_exampledir}/chemistry
# computer
install -d $RPM_BUILD_ROOT%{_exampledir}/computer
install %{SOURCE4} %{SOURCE5} %{SOURCE6} %{SOURCE7} %{SOURCE8} %{SOURCE9} \
	%{SOURCE10} %{SOURCE11} %{SOURCE12} %{SOURCE13} %{SOURCE14} %{SOURCE15} \
	%{SOURCE16} %{SOURCE17} %{SOURCE18} %{SOURCE19} %{SOURCE20} %{SOURCE21} \
	$RPM_BUILD_ROOT%{_exampledir}/computer
# electrical
install -d $RPM_BUILD_ROOT%{_exampledir}/electrical
install %{SOURCE22} %{SOURCE23} %{SOURCE24} %{SOURCE25} %{SOURCE26} %{SOURCE27} \
	%{SOURCE28} %{SOURCE29} %{SOURCE30} %{SOURCE31} %{SOURCE32} %{SOURCE33} \
	%{SOURCE34} %{SOURCE35} %{SOURCE36} %{SOURCE37} %{SOURCE38} %{SOURCE39} \
	$RPM_BUILD_ROOT%{_exampledir}/electrical
# mathematics
install -d $RPM_BUILD_ROOT%{_exampledir}/mathematics
install	%{SOURCE40} %{SOURCE41} %{SOURCE42} %{SOURCE43} %{SOURCE44} %{SOURCE45} \
	%{SOURCE46} %{SOURCE47} %{SOURCE48} %{SOURCE49} %{SOURCE50} %{SOURCE51} \
	%{SOURCE52} %{SOURCE53} \
	$RPM_BUILD_ROOT%{_exampledir}/mathematics
# physics
install -d $RPM_BUILD_ROOT%{_exampledir}/physics
install	%{SOURCE54} %{SOURCE55} %{SOURCE56} %{SOURCE57} %{SOURCE58} %{SOURCE59} \
	%{SOURCE60} %{SOURCE61} %{SOURCE62} %{SOURCE63} %{SOURCE64} %{SOURCE65} \
	$RPM_BUILD_ROOT%{_exampledir}/physics
# statistics
install -d $RPM_BUILD_ROOT%{_exampledir}/statistics
install	%{SOURCE66} %{SOURCE67} %{SOURCE68} %{SOURCE69} %{SOURCE70} %{SOURCE71} \
	$RPM_BUILD_ROOT%{_exampledir}/statistics

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%dir %{_datadir}/texmf/doc/latex/tikz
%dir %{_exampledir}
%{_exampledir}/README

%files chemistry
%defattr(644,root,root,755)
%dir %{_exampledir}/chemistry
%{_exampledir}/chemistry/*

%files computer
%defattr(644,root,root,755)
%dir %{_exampledir}/computer
%{_exampledir}/computer/*

%files electrical
%defattr(644,root,root,755)
%dir %{_exampledir}/electrical
%{_exampledir}/electrical/*

%files mathematics
%defattr(644,root,root,755)
%dir %{_exampledir}/mathematics
%{_exampledir}/mathematics/*

%files physics
%defattr(644,root,root,755)
%dir %{_exampledir}/physics
%{_exampledir}/physics/*

%files statistics
%defattr(644,root,root,755)
%dir %{_exampledir}/statistics
%{_exampledir}/statistics/*
