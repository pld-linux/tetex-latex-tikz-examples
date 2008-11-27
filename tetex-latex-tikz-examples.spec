# TODO: there are many examples outside "Technical Areas"
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
Source100:	%{pdfdir}/circuitikz.pdf
Source101:	%{texdir}/circuitikz.tex
Source102:	%{pdfdir}/control-system-principles.pdf
Source103:	%{texdir}/control-system-principles.tex
Source104:	%{pdfdir}/circuit-decorations.pdf
Source105:	%{texdir}/circuit-decorations.tex
Source106:	%{pdfdir}/FIR-filter.pdf
Source107:	%{texdir}/FIR-filter.tex
Source108:	%{pdfdir}/logic-circuits-library.pdf
Source109:	%{texdir}/logic-circuits-library.tex
Source110:	%{pdfdir}/radix2fft.pdf
Source111:	%{texdir}/radix2fft.tex
Source112:	%{pdfdir}/schemabloc.pdf
Source113:	%{texdir}/schemabloc.tex
Source114:	%{pdfdir}/signal-flow-building-blocks.pdf
Source115:	%{texdir}/signal-flow-building-blocks.tex
Source116:	%{pdfdir}/simple-circuit-schematics-symbols.pdf
Source117:	%{texdir}/simple-circuit-schematics-symbols.tex
# mathematics
Source200:	%{pdfdir}/animated-set-intersection.pdf
Source201:	%{texdir}/animated-set-intersection.tex
Source202:	%{pdfdir}/tutorial.pdf
Source203:	%{texdir}/tutorial.tex
Source204:	%{pdfdir}/hilbert-curve.pdf
Source205:	%{texdir}/hilbert-curve.tex
Source206:	%{pdfdir}/parallel-lines.pdf
Source207:	%{texdir}/parallel-lines.tex
Source208:	%{pdfdir}/polygon-division.pdf
Source209:	%{texdir}/polygon-division.tex
Source210:	%{pdfdir}/sign-diagram.pdf
Source211:	%{texdir}/sign-diagram.tex
Source212:	%{pdfdir}/star-graph.pdf
Source213:	%{texdir}/star-graph.tex
Source214:	%{pdfdir}/lune-of-hippocrates.pdf
Source215:	%{texdir}/lune-of-hippocrates.tex
Source216:	%{pdfdir}/tkz-2d.pdf
Source217:	%{texdir}/tkz-2d.tex
# physics
Source300:	%{pdfdir}/beamer-arrows.pdf
Source301:	%{texdir}/beamer-arrows.tex
Source302:	%{pdfdir}/feynman-diagram.pdf
Source303:	%{texdir}/feynman-diagram.tex
Source304:	%{pdfdir}/free-body-diagrams.pdf
Source305:	%{texdir}/free-body-diagrams.tex
Source306:	%{pdfdir}/gamma-interaction.pdf
Source307:	%{texdir}/gamma-interaction.tex
Source308:	%{pdfdir}/global-nodes.pdf
Source309:	%{texdir}/global-nodes.tex
Source310:	%{pdfdir}/oblique-incidence.pdf
Source311:	%{texdir}/oblique-incidence.tex
# statistics
Source400:	%{pdfdir}/animated-distributions.pdf
Source401:	%{texdir}/animated-distributions.tex
Source402:	%{pdfdir}/box-and-whisker-plot.pdf
Source403:	%{texdir}/box-and-whisker-plot.tex
Source404:	%{pdfdir}/standard-deviation.pdf
Source405:	%{texdir}/standard-deviation.tex
Requires:	tetex-latex
# 2.00 is required so please don't delete it!
Requires:	tetex-pgf >= 2.00
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
Suggests:	tetex-latex-mhchem

%description chemistry
TikZ chemistry examples

%description chemistry -l hu.UTF-8
TikZ kémiai példák


%package computer
Summary:	TikZ computer science examples
Summary(hu.UTF-8):	TikZ számítógép-tudományi példák
Group:		Applications/Publishing/TeX
Suggests:	tetex-latex-beamer
Suggests:	tetex-latex-pgf-umlsd
Suggests:	tetex-latex-tikz-inet

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
Suggests:	tetex-latex-electcomp
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
Suggests:	tetex-latex-beamer

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
install %{SOURCE100} %{SOURCE101} %{SOURCE102} %{SOURCE103} %{SOURCE104} %{SOURCE105} \
	%{SOURCE106} %{SOURCE107} %{SOURCE108} %{SOURCE109} %{SOURCE110} %{SOURCE111} \
	%{SOURCE112} %{SOURCE113} %{SOURCE114} %{SOURCE115} %{SOURCE116} %{SOURCE117} \
	$RPM_BUILD_ROOT%{_exampledir}/electrical
# mathematics
install -d $RPM_BUILD_ROOT%{_exampledir}/mathematics
install	%{SOURCE200} %{SOURCE201} %{SOURCE202} %{SOURCE203} %{SOURCE204} %{SOURCE205} \
	%{SOURCE206} %{SOURCE207} %{SOURCE208} %{SOURCE209} %{SOURCE210} %{SOURCE211} \
	%{SOURCE212} %{SOURCE213} %{SOURCE214} %{SOURCE215} %{SOURCE216} %{SOURCE217} \
	$RPM_BUILD_ROOT%{_exampledir}/mathematics
# physics
install -d $RPM_BUILD_ROOT%{_exampledir}/physics
install	%{SOURCE300} %{SOURCE301} %{SOURCE302} %{SOURCE303} %{SOURCE304} %{SOURCE305} \
	%{SOURCE306} %{SOURCE307} %{SOURCE308} %{SOURCE309} %{SOURCE310} %{SOURCE311} \
	$RPM_BUILD_ROOT%{_exampledir}/physics
# statistics
install -d $RPM_BUILD_ROOT%{_exampledir}/statistics
install	%{SOURCE400} %{SOURCE401} %{SOURCE402} %{SOURCE403} %{SOURCE404} %{SOURCE405} \
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
