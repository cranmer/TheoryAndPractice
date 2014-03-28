Title: Using the INSPIRE API to generate AltMetric badges
date: 2014-03-28 10:53
Slug: inspire-altmetric-api
Category: Blog
Authors: Kyle Cranmer

I updated my [Research](/pages/Research.html) page to include the [Altmetric](altmetric.com) badges to highlight a few papers that I've been involved with that had some impact outside of high energy physics.  On the side, I was wanting to try out the [INSPIRE](http://inspirehep.net) API.  So I put the two together to make a 
[little tool](https://github.com/cranmer/play/blob/master/INSPIRE_AltMetric/inspireToAltMetric.py) that generates a little table of paper title and altmetric badge for a given author (me in this case).  

Maybe I'll try to deploy that as a little flask service. I'd also like to make a scatter plot of the number of citations to the altmetric score, but the current INSPIRE API doesn't give that information (though it is comming soon).

<!--http://api.altmetric.com/embeds.html-->
<script type='text/javascript' src='https://d1bxh8uas1mnw7.cloudfront.net/assets/embed.js'></script>


- - - 
<div class="row">
	<div  class="col-md-4">
		Software for statistical data analysis used in Higgs searches
	</div>
	<div  class='col-md-8'> 
		<div class='altmetric-embed' data-badge-type='donut' 
		data-badge-details='right' data-doi='10.1088/1742-6596/490/1/012229'></div>
	</div>
</div>
- - - 
<div class="row">
	<div  class="col-md-4">
		Search for Higgs boson decays to a photon and a Z boson in pp collisions at $\sqrt{s}$=7 and 8 TeV with the ATLAS detector
	</div>
	<div  class='col-md-8'> 
		<div class='altmetric-embed' data-badge-type='donut' 
		data-badge-details='right' data-doi='10.1016/j.physletb.2014.03.015'></div>
	</div>
</div>
- - - 
<div class="row">
	<div  class="col-md-4">
		Search for a Multi-Higgs Boson Cascade in $W^+W^− b\bar{b}$ events with the ATLAS detector in pp collisions at √s = 8 TeV
	</div>
	<div  class='col-md-8'> 
		<div class='altmetric-embed' data-badge-type='donut' 
		data-badge-details='right' data-doi='10.1103/PhysRevD.89.032002'></div>
	</div>
</div>
- - - 
<div class="row">
	<div  class="col-md-4">
		Standalone vertex finding in the ATLAS muon spectrometer
	</div>
	<div  class='col-md-8'> 
		<div class='altmetric-embed' data-badge-type='donut' 
		data-badge-details='right' data-doi='10.1088/1748-0221/9/02/P02001'></div>
	</div>
</div>
- - - 
<div class="row">
	<div  class="col-md-4">
		Measurement of the top quark pair production charge asymmetry in proton-proton collisions at $\sqrt{s}$ = 7 TeV using the ATLAS detector
	</div>
	<div  class='col-md-8'> 
		<div class='altmetric-embed' data-badge-type='donut' 
		data-badge-details='right' data-doi='10.1007/JHEP02(2014)107'></div>
	</div>
</div>
- - - 
<div class="row">
	<div  class="col-md-4">
		Search for Quantum Black-Hole Production in High-Invariant-Mass Lepton+Jet Final States Using Proton-Proton Collisions at $\sqrt{s} = 8$ TeV and the ATLAS Detector
	</div>
	<div  class='col-md-8'> 
		<div class='altmetric-embed' data-badge-type='donut' 
		data-badge-details='right' data-doi='10.1103/PhysRevLett.112.091804'></div>
	</div>
</div>
- - - 
<div class="row">
	<div  class="col-md-4">
		Search for long-lived stopped R-hadrons decaying out-of-time with pp collisions using the ATLAS detector
	</div>
	<div  class='col-md-8'> 
		<div class='altmetric-embed' data-badge-type='donut' 
		data-badge-details='right' data-doi='10.1103/PhysRevD.88.112003'></div>
	</div>
</div>
- - - 
<div class="row">
	<div  class="col-md-4">
		Measurement of the mass difference between top and anti-top quarks in pp collisions at $\sqrt(s) = 7$ TeV using the ATLAS detector
	</div>
	<div  class='col-md-8'> 
		<div class='altmetric-embed' data-badge-type='donut' 
		data-badge-details='right' data-doi='10.1016/j.physletb.2013.12.010'></div>
	</div>
</div>
- - - 
<div class="row">
	<div  class="col-md-4">
		Search for charginos nearly mass-degenerate with the lightest neutralino based on a disappearing-track signature in pp collisions at $\sqrt{s}$ = 8 TeV with the ATLAS detector
	</div>
	<div  class='col-md-8'> 
		<div class='altmetric-embed' data-badge-type='donut' 
		data-badge-details='right' data-doi='10.1103/PhysRevD.88.112006'></div>
	</div>
</div>
- - - 
<div class="row">
	<div  class="col-md-4">
		Search for dark matter in events with a hadronically decaying W or Z boson and missing transverse momentum in pp collisions at $\sqrt{s}$=8 TeV with the ATLAS detector
	</div>
	<div  class='col-md-8'> 
		<div class='altmetric-embed' data-badge-type='donut' 
		data-badge-details='right' data-doi='10.1103/PhysRevLett.112.041802'></div>
	</div>
</div>
- - - 
<div class="row">
	<div  class="col-md-4">
		Search for new phenomena in photon+jet events collected in proton--proton collisions at $\sqrt{s}$ = 8 TeV with the ATLAS detector
	</div>
	<div  class='col-md-8'> 
		<div class='altmetric-embed' data-badge-type='donut' 
		data-badge-details='right' data-doi='10.1016/j.physletb.2013.12.029'></div>
	</div>
</div>
- - - 
<div class="row">
	<div  class="col-md-4">
		Search for microscopic black holes in a like-sign dimuon final state using large track multiplicity with the ATLAS detector
	</div>
	<div  class='col-md-8'> 
		<div class='altmetric-embed' data-badge-type='donut' 
		data-badge-details='right' data-doi='10.1103/PhysRevD.88.072001'></div>
	</div>
</div>
- - - 
<div class="row">
	<div  class="col-md-4">
		Search for direct third-generation squark pair production in final states with missing transverse momentum and two $b$-jets in $\sqrt{s} =$ 8 TeV $pp$ collisions with the ATLAS detector
	</div>
	<div  class='col-md-8'> 
		<div class='altmetric-embed' data-badge-type='donut' 
		data-badge-details='right' data-doi='10.1007/JHEP10(2013)189'></div>
	</div>
</div>
- - - 
<div class="row">
	<div  class="col-md-4">
		Search for new phenomena in final states with large jet multiplicities and missing transverse momentum at sqrt(s)=8 TeV proton-proton collisions using the ATLAS experiment
	</div>
	<div  class='col-md-8'> 
		<div class='altmetric-embed' data-badge-type='donut' 
		data-badge-details='right' data-doi='10.1007/JHEP10(2013)130'></div>
	</div>
</div>
- - - 
<div class="row">
	<div  class="col-md-4">
		Search for excited electrons and muons in $\sqrt{s}$=8 TeV proton-proton collisions with the ATLAS detector
	</div>
	<div  class='col-md-8'> 
		<div class='altmetric-embed' data-badge-type='donut' 
		data-badge-details='right' data-doi='10.1088/1367-2630/15/9/093011'></div>
	</div>
</div>
- - - 
<div class="row">
	<div  class="col-md-4">
		Dynamics of isolated-photon plus jet production in pp collisions at $\sqrt(s)=7$ TeV with the ATLAS detector
	</div>
	<div  class='col-md-8'> 
		<div class='altmetric-embed' data-badge-type='donut' 
		data-badge-details='right' data-doi='10.1016/j.nuclphysb.2013.07.025'></div>
	</div>
</div>
- - - 
<div class="row">
	<div  class="col-md-4">
		Measurement of top quark polarization in top-antitop events from proton-proton collisions at $\sqrt{s}$ = 7 TeV using the ATLAS detector
	</div>
	<div  class='col-md-8'> 
		<div class='altmetric-embed' data-badge-type='donut' 
		data-badge-details='right' data-doi='10.1103/PhysRevLett.111.232002'></div>
	</div>
</div>
- - - 
<div class="row">
	<div  class="col-md-4">
		Measurement of jet shapes in top-quark pair events at $\sqrt{s}$ = 7 TeV using the ATLAS detector
	</div>
	<div  class='col-md-8'> 
		<div class='altmetric-embed' data-badge-type='donut' 
		data-badge-details='right' data-doi='10.1140/epjc/s10052-013-2676-3'></div>
	</div>
</div>
- - - 
<div class="row">
	<div  class="col-md-4">
		Measurement of the top quark charge in $pp$ collisions at $\sqrt{s} =$ 7 TeV with the ATLAS detector
	</div>
	<div  class='col-md-8'> 
		<div class='altmetric-embed' data-badge-type='donut' 
		data-badge-details='right' data-doi='10.1007/JHEP11(2013)031'></div>
	</div>
</div>
- - - 
<div class="row">
	<div  class="col-md-4">
		Evidence for the spin-0 nature of the Higgs boson using ATLAS data
	</div>
	<div  class='col-md-8'> 
		<div class='altmetric-embed' data-badge-type='donut' 
		data-badge-details='right' data-doi='10.1016/j.physletb.2013.08.026'></div>
	</div>
</div>
- - - 
<div class="row">
	<div  class="col-md-4">
		Measurements of Higgs boson production and couplings in diboson final states with the ATLAS detector at the LHC
	</div>
	<div  class='col-md-8'> 
		<div class='altmetric-embed' data-badge-type='donut' 
		data-badge-details='right' data-doi='10.1016/j.physletb.2013.08.010'></div>
	</div>
</div>
- - - 
<div class="row">
	<div  class="col-md-4">
		Measurement of the differential cross-section of $B^{+}$ meson production in pp collisions at $\sqrt{s}$ = 7 TeV at ATLAS
	</div>
	<div  class='col-md-8'> 
		<div class='altmetric-embed' data-badge-type='donut' 
		data-badge-details='right' data-doi='10.1007/JHEP10(2013)042'></div>
	</div>
</div>
- - - 
<div class="row">
	<div  class="col-md-4">
		Measurement of the Azimuthal Angle Dependence of Inclusive Jet Yields in Pb+Pb Collisions at $\sqrt{s_{NN}}$= 2.76 TeV with the ATLAS detector
	</div>
	<div  class='col-md-8'> 
		<div class='altmetric-embed' data-badge-type='donut' 
		data-badge-details='right' data-doi='10.1103/PhysRevLett.111.152301'></div>
	</div>
</div>
- - - 
<div class="row">
	<div  class="col-md-4">
		Performance of jet substructure techniques for large-$R$ jets in proton-proton collisions at $\sqrt{s}$ = 7 TeV using the ATLAS detector
	</div>
	<div  class='col-md-8'> 
		<div class='altmetric-embed' data-badge-type='donut' 
		data-badge-details='right' data-doi='10.1007/JHEP09(2013)076'></div>
	</div>
</div>
- - - 
<div class="row">
	<div  class="col-md-4">
		Measurement of the high-mass Drell--Yan differential cross-section in pp collisions at $\sqrt{s}$=7 TeV with the ATLAS detector
	</div>
	<div  class='col-md-8'> 
		<div class='altmetric-embed' data-badge-type='donut' 
		data-badge-details='right' data-doi='10.1016/j.physletb.2013.07.049'></div>
	</div>
</div>
- - - 
<div class="row">
	<div  class="col-md-4">
		Measurement of the distributions of event-by-event flow harmonics in lead-lead collisions at = 2.76 TeV with the ATLAS detector at the LHC
	</div>
	<div  class='col-md-8'> 
		<div class='altmetric-embed' data-badge-type='donut' 
		data-badge-details='right' data-doi='10.1007/JHEP11(2013)183'></div>
	</div>
</div>
- - - 
<div class="row">
	<div  class="col-md-4">
		Search for $t\bar t$ resonances in the lepton plus jets final state with ATLAS using 4.7 fb$^{-1}$ of $pp$ collisions at $\sqrt{s} = 7$ TeV
	</div>
	<div  class='col-md-8'> 
		<div class='altmetric-embed' data-badge-type='donut' 
		data-badge-details='right' data-doi='10.1103/PhysRevD.88.012004'></div>
	</div>
</div>
- - - 
<div class="row">
	<div  class="col-md-4">
		Triggers for displaced decays of long-lived neutral particles in the ATLAS detector
	</div>
	<div  class='col-md-8'> 
		<div class='altmetric-embed' data-badge-type='donut' 
		data-badge-details='right' data-doi='10.1088/1748-0221/8/07/P07015'></div>
	</div>
</div>
- - - 
<div class="row">
	<div  class="col-md-4">
		Search for resonant diboson production in the WW/WZ→ℓνjj decay channels with the ATLAS detector at $\sqrt{s}$ = 7  TeV
	</div>
	<div  class='col-md-8'> 
		<div class='altmetric-embed' data-badge-type='donut' 
		data-badge-details='right' data-doi='10.1103/PhysRevD.87.112006'></div>
	</div>
</div>
- - - 
<div class="row">
	<div  class="col-md-4">
		Measurement of the production cross section of jets in association with a Z boson in pp collisions at $\sqrt{s}$ = 7 TeV with the ATLAS detector
	</div>
	<div  class='col-md-8'> 
		<div class='altmetric-embed' data-badge-type='donut' 
		data-badge-details='right' data-doi='10.1007/JHEP07(2013)032'></div>
	</div>
</div>
- - - 
<div class="row">
	<div  class="col-md-4">
		Search for nonpointing photons in the diphoton and $E^{miss}_T$ final state in $\sqrt{s}$=7  TeV proton-proton collisions using the ATLAS detector
	</div>
	<div  class='col-md-8'> 
		<div class='altmetric-embed' data-badge-type='donut' 
		data-badge-details='right' data-doi='10.1103/PhysRevD.88.012001'></div>
	</div>
</div>
- - - 
<div class="row">
	<div  class="col-md-4">
		Measurement of the inclusive jet cross section in pp collisions at sqrt(s)=2.76 TeV and comparison to the inclusive jet cross section at sqrt(s)=7 TeV using the ATLAS detector
	</div>
	<div  class='col-md-8'> 
		<div class='altmetric-embed' data-badge-type='donut' 
		data-badge-details='right' data-doi='10.1140/epjc/s10052-013-2509-4'></div>
	</div>
</div>
- - - 
<div class="row">
	<div  class="col-md-4">
		A particle consistent with the Higgs Boson observed with the ATLAS Detector at the Large Hadron Collider
	</div>
	<div  class='col-md-8'> 
		<div class='altmetric-embed' data-badge-type='donut' 
		data-badge-details='right' data-doi='10.1126/science.1232005'></div>
	</div>
</div>
- - - 
<div class="row">
	<div  class="col-md-4">
		Measurement with the ATLAS detector of multi-particle azimuthal correlations in p+Pb collisions at $\sqrt{s_{NN}}$=5.02 TeV
	</div>
	<div  class='col-md-8'> 
		<div class='altmetric-embed' data-badge-type='donut' 
		data-badge-details='right' data-doi='10.1016/j.physletb.2013.06.057'></div>
	</div>
</div>
- - - 
<div class="row">
	<div  class="col-md-4">
		Search for third generation scalar leptoquarks in pp collisions at $\sqrt{s}$ = 7 TeV with the ATLAS detector
	</div>
	<div  class='col-md-8'> 
		<div class='altmetric-embed' data-badge-type='donut' 
		data-badge-details='right' data-doi='10.1007/JHEP06(2013)033'></div>
	</div>
</div>
- - - 
<div class="row">
	<div  class="col-md-4">
		Characterisation and mitigation of beam-induced backgrounds observed in the ATLAS detector during the 2011 proton-proton run
	</div>
	<div  class='col-md-8'> 
		<div class='altmetric-embed' data-badge-type='donut' 
		data-badge-details='right' data-doi='10.1088/1748-0221/8/07/P07004'></div>
	</div>
</div>
- - - 
<div class="row">
	<div  class="col-md-4">
		Search for WH production with a light Higgs boson decaying to prompt electron-jets in proton-proton collisions at $\sqrt{s}$=7 TeV with the ATLAS detector
	</div>
	<div  class='col-md-8'> 
		<div class='altmetric-embed' data-badge-type='donut' 
		data-badge-details='right' data-doi='10.1088/1367-2630/15/4/043009'></div>
	</div>
</div>
- - - 
<div class="row">
	<div  class="col-md-4">
		Improved luminosity determination in $pp$ collisions at $\sqrt{s}$ = 7 TeV using the ATLAS detector at the LHC
	</div>
	<div  class='col-md-8'> 
		<div class='altmetric-embed' data-badge-type='donut' 
		data-badge-details='right' data-doi='10.1140/epjc/s10052-013-2518-3'></div>
	</div>
</div>
- - - 
<div class="row">
	<div  class="col-md-4">
		Search for a light charged Higgs boson in the decay channel $H^+ \to c\bar{s}$ in $t\bar{t}$ events using pp collisions at $\sqrt{s}$ = 7 TeV with the ATLAS detector
	</div>
	<div  class='col-md-8'> 
		<div class='altmetric-embed' data-badge-type='donut' 
		data-badge-details='right' data-doi='10.1140/epjc/s10052-013-2465-z'></div>
	</div>
</div>
- - - 
<div class="row">
	<div  class="col-md-4">
		Electroweak Measurements in Electron-Positron Collisions at W-Boson-Pair Energies at LEP
	</div>
	<div  class='col-md-8'> 
		<div class='altmetric-embed' data-badge-type='donut' 
		data-badge-details='right' data-doi='10.1016/j.physrep.2013.07.004'></div>
	</div>
</div>
- - - 
<div class="row">
	<div  class="col-md-4">
		Measurement of the cross-section for W boson production in association with b-jets in pp collisions at $\sqrt{s}$ = 7 TeV with the ATLAS detector
	</div>
	<div  class='col-md-8'> 
		<div class='altmetric-embed' data-badge-type='donut' 
		data-badge-details='right' data-doi='10.1007/JHEP06(2013)084'></div>
	</div>
</div>
- - - 
<div class="row">
	<div  class="col-md-4">
		Measurement of kT splitting scales in W->lv events at sqrt(s)=7 TeV with the ATLAS detector
	</div>
	<div  class='col-md-8'> 
		<div class='altmetric-embed' data-badge-type='donut' 
		data-badge-details='right' data-doi='10.1140/epjc/s10052-013-2432-8'></div>
	</div>
</div>
- - - 
<div class="row">
	<div  class="col-md-4">
		Measurements of Wγ and Zγ production in pp collisions at $\sqrt{s}$=7  TeV with the ATLAS detector at the LHC
	</div>
	<div  class='col-md-8'> 
		<div class='altmetric-embed' data-badge-type='donut' 
		data-badge-details='right' data-doi='10.1103/PhysRevD.87.112003'></div>
	</div>
</div>
- - - 
<div class="row">
	<div  class="col-md-4">
		Measurement of hard double-parton interactions in $W(\to l\nu)$+ 2 jet events at $\sqrt{s}$=7 TeV with the ATLAS detector
	</div>
	<div  class='col-md-8'> 
		<div class='altmetric-embed' data-badge-type='donut' 
		data-badge-details='right' data-doi='10.1088/1367-2630/15/3/033038'></div>
	</div>
</div>
- - - 
<div class="row">
	<div  class="col-md-4">
		Search for Charged Higgs bosons: Combined Results Using LEP Data
	</div>
	<div  class='col-md-8'> 
		<div class='altmetric-embed' data-badge-type='donut' 
		data-badge-details='right' data-doi='10.1140/epjc/s10052-013-2463-1'></div>
	</div>
</div>
- - - 
<div class="row">
	<div  class="col-md-4">
		Search for long-lived, multi-charged particles in pp collisions at $\sqrt{s}$=7 TeV using the ATLAS detector
	</div>
	<div  class='col-md-8'> 
		<div class='altmetric-embed' data-badge-type='donut' 
		data-badge-details='right' data-doi='10.1016/j.physletb.2013.04.036'></div>
	</div>
</div>
- - - 
<div class="row">
	<div  class="col-md-4">
		Search for single $b^*$-quark production with the ATLAS detector at $\sqrt{s}=7$ TeV
	</div>
	<div  class='col-md-8'> 
		<div class='altmetric-embed' data-badge-type='donut' 
		data-badge-details='right' data-doi='10.1016/j.physletb.2013.03.016'></div>
	</div>
</div>
- - - 
<div class="row">
	<div  class="col-md-4">
		Multi-channel search for squarks and gluinos in $\sqrt{s}=7$ TeV $pp$ collisions with the ATLAS detector
	</div>
	<div  class='col-md-8'> 
		<div class='altmetric-embed' data-badge-type='donut' 
		data-badge-details='right' data-doi='10.1140/epjc/s10052-013-2362-5'></div>
	</div>
</div>
- - - 
<div class="row">
	<div  class="col-md-4">
		A search for prompt lepton-jets in $pp$ collisions at $\sqrt{s}=7$ TeV with the ATLAS detector
	</div>
	<div  class='col-md-8'> 
		<div class='altmetric-embed' data-badge-type='donut' 
		data-badge-details='right' data-doi='10.1016/j.physletb.2013.01.034'></div>
	</div>
</div>
- - - 
<div class="row">
	<div  class="col-md-4">
		Observation of Associated Near-side and Away-side Long-range Correlations in $\sqrt{s_{NN}}$=5.02 TeV Proton-lead Collisions with the ATLAS Detector
	</div>
	<div  class='col-md-8'> 
		<div class='altmetric-embed' data-badge-type='donut' 
		data-badge-details='right' data-doi='10.1103/PhysRevLett.110.182302'></div>
	</div>
</div>
- - - 
<div class="row">
	<div  class="col-md-4">
		Search for charged Higgs bosons through the violation of lepton universality in $t\bar{t}$ events using $pp$ collision data at $\sqrt{s}=7$ TeV with the ATLAS experiment
	</div>
	<div  class='col-md-8'> 
		<div class='altmetric-embed' data-badge-type='donut' 
		data-badge-details='right' data-doi='10.1007/JHEP03(2013)076'></div>
	</div>
</div>
- - - 
<div class="row">
	<div  class="col-md-4">
		Search for a heavy narrow resonance decaying to $e \mu$, $e \tau$, or $\mu \tau$ with the ATLAS detector in $\sqrt{s}=7$ TeV $pp$ collisions at the LHC
	</div>
	<div  class='col-md-8'> 
		<div class='altmetric-embed' data-badge-type='donut' 
		data-badge-details='right' data-doi='10.1016/j.physletb.2013.04.035'></div>
	</div>
</div>
- - - 
<div class="row">
	<div  class="col-md-4">
		Measurement of Upsilon production in 7 TeV pp collisions at ATLAS
	</div>
	<div  class='col-md-8'> 
		<div class='altmetric-embed' data-badge-type='donut' 
		data-badge-details='right' data-doi='10.1103/PhysRevD.87.052004'></div>
	</div>
</div>
- - - 
<div class="row">
	<div  class="col-md-4">
		Measurement of the ttbar production cross section in the tau+jets channel using the ATLAS detector
	</div>
	<div  class='col-md-8'> 
		<div class='altmetric-embed' data-badge-type='donut' 
		data-badge-details='right' data-doi='10.1140/epjc/s10052-013-2328-7'></div>
	</div>
</div>
- - - 
<div class="row">
	<div  class="col-md-4">
		Search for the neutral Higgs bosons of the Minimal Supersymmetric Standard Model in $pp$ collisions at $\sqrt{s}=7$ TeV with the ATLAS detector
	</div>
	<div  class='col-md-8'> 
		<div class='altmetric-embed' data-badge-type='donut' 
		data-badge-details='right' data-doi='10.1007/JHEP02(2013)095'></div>
	</div>
</div>
- - - 
<div class="row">
	<div  class="col-md-4">
		Measurement of angular correlations in Drell-Yan lepton pairs to probe Z/gamma* boson transverse momentum at sqrt(s)=7 TeV with the ATLAS detector
	</div>
	<div  class='col-md-8'> 
		<div class='altmetric-embed' data-badge-type='donut' 
		data-badge-details='right' data-doi='10.1016/j.physletb.2013.01.054'></div>
	</div>
</div>
- - - 
<div class="row">
	<div  class="col-md-4">
		Search for new phenomena in events with three charged leptons at $/sqrt{s}$ = 7 TeV with the ATLAS detector
	</div>
	<div  class='col-md-8'> 
		<div class='altmetric-embed' data-badge-type='donut' 
		data-badge-details='right' data-doi='10.1103/PhysRevD.87.052002'></div>
	</div>
</div>
- - - 
<div class="row">
	<div  class="col-md-4">
		Measurement of $ZZ$ production in $pp$ collisions at $\sqrt{s}=7$ TeV and limits on anomalous $ZZZ$ and $ZZ\gamma$ couplings with the ATLAS detector
	</div>
	<div  class='col-md-8'> 
		<div class='altmetric-embed' data-badge-type='donut' 
		data-badge-details='right' data-doi='10.1007/JHEP03(2013)128'></div>
	</div>
</div>
- - - 
<div class="row">
	<div  class="col-md-4">
		Search for resonances decaying into top-quark pairs using fully hadronic decays in $pp$ collisions with ATLAS at $\sqrt{s}=7$ TeV
	</div>
	<div  class='col-md-8'> 
		<div class='altmetric-embed' data-badge-type='donut' 
		data-badge-details='right' data-doi='10.1007/JHEP01(2013)116'></div>
	</div>
</div>
- - - 
<div class="row">
	<div  class="col-md-4">
		Measurement of isolated-photon pair production in $pp$ collisions at $\sqrt{s}=7$ TeV with the ATLAS detector
	</div>
	<div  class='col-md-8'> 
		<div class='altmetric-embed' data-badge-type='donut' 
		data-badge-details='right' data-doi='10.1007/JHEP01(2013)086'></div>
	</div>
</div>
- - - 
<div class="row">
	<div  class="col-md-4">
		Searches for heavy long-lived sleptons and R-Hadrons with the ATLAS detector in $pp$ collisions at $\sqrt{s}=7$ TeV
	</div>
	<div  class='col-md-8'> 
		<div class='altmetric-embed' data-badge-type='donut' 
		data-badge-details='right' data-doi='10.1016/j.physletb.2013.02.015'></div>
	</div>
</div>
- - - 
<div class="row">
	<div  class="col-md-4">
		Search for supersymmetry in events with photons, bottom quarks, and missing transverse momentum in proton-proton collisions at a centre-of-mass energy of 7 TeV with the ATLAS detector
	</div>
	<div  class='col-md-8'> 
		<div class='altmetric-embed' data-badge-type='donut' 
		data-badge-details='right' data-doi='10.1016/j.physletb.2013.01.041'></div>
	</div>
</div>
- - - 
<div class="row">
	<div  class="col-md-4">
		Search for contact interactions and large extra dimensions in dilepton events from $pp$ collisions at $\sqrt{s}=7$ TeV with the ATLAS detector
	</div>
	<div  class='col-md-8'> 
		<div class='altmetric-embed' data-badge-type='donut' 
		data-badge-details='right' data-doi='10.1103/PhysRevD.87.015010'></div>
	</div>
</div>
- - - 
<div class="row">
	<div  class="col-md-4">
		Search for Extra Dimensions in diphoton events using proton-proton collisions recorded at $\sqrt{s}=7$ TeV with the ATLAS detector at the LHC
	</div>
	<div  class='col-md-8'> 
		<div class='altmetric-embed' data-badge-type='donut' 
		data-badge-details='right' data-doi='10.1088/1367-2630/15/4/043007'></div>
	</div>
</div>
- - - 
<div class="row">
	<div  class="col-md-4">
		Muon Detection Based on a Hadronic Calorimeter
	</div>
	<div  class='col-md-8'> 
		<div class='altmetric-embed' data-badge-type='donut' 
		data-badge-details='right' data-doi='10.1109/NSSMIC.2010.5873863'></div>
	</div>
</div>
- - - 
<div class="row">
	<div  class="col-md-4">
		Search for long-lived, heavy particles in final states with a muon and multi-track displaced vertex in proton-proton collisions at $\sqrt{s}=7$ TeV with the ATLAS detector
	</div>
	<div  class='col-md-8'> 
		<div class='altmetric-embed' data-badge-type='donut' 
		data-badge-details='right' data-doi='10.1016/j.physletb.2013.01.042'></div>
	</div>
</div>
- - - 
<div class="row">
	<div  class="col-md-4">
		A search for high-mass resonances decaying to $\tau^+\tau^-$ in $pp$ collisions at $\sqrt{s}=7$ TeV with the ATLAS detector
	</div>
	<div  class='col-md-8'> 
		<div class='altmetric-embed' data-badge-type='donut' 
		data-badge-details='right' data-doi='10.1016/j.physletb.2013.01.040'></div>
	</div>
</div>
- - - 
<div class="row">
	<div  class="col-md-4">
		Measurement of $Z$ boson Production in Pb+Pb Collisions at $\sqrt{s_{NN}}=2.76$ TeV with the ATLAS Detector
	</div>
	<div  class='col-md-8'> 
		<div class='altmetric-embed' data-badge-type='donut' 
		data-badge-details='right' data-doi='10.1103/PhysRevLett.110.022301'></div>
	</div>
</div>
- - - 
<div class="row">
	<div  class="col-md-4">
		Jet energy resolution in proton-proton collisions at $\sqrt{s}=7$ TeV recorded in 2010 with the ATLAS detector
	</div>
	<div  class='col-md-8'> 
		<div class='altmetric-embed' data-badge-type='donut' 
		data-badge-details='right' data-doi='10.1140/epjc/s10052-013-2306-0'></div>
	</div>
</div>
- - - 
<div class="row">
	<div  class="col-md-4">
		Search for pair production of heavy top-like quarks decaying to a high-pT $W$ boson and a $b$ quark in the lepton plus jets final state at $\sqrt{s}$=7 TeV with the ATLAS detector
	</div>
	<div  class='col-md-8'> 
		<div class='altmetric-embed' data-badge-type='donut' 
		data-badge-details='right' data-doi='10.1016/j.physletb.2012.11.071'></div>
	</div>
</div>
- - - 
<div class="row">
	<div  class="col-md-4">
		Search for doubly-charged Higgs bosons in like-sign dilepton final states at $\sqrt{s}=7$ TeV with the ATLAS detector
	</div>
	<div  class='col-md-8'> 
		<div class='altmetric-embed' data-badge-type='donut' 
		data-badge-details='right' data-doi='10.1140/epjc/s10052-012-2244-2'></div>
	</div>
</div>
- - - 
<div class="row">
	<div  class="col-md-4">
		Search for pair-produced massive coloured scalars in four-jet final states with the ATLAS detector in proton-proton collisions at $\sqrt{s}=7$ TeV
	</div>
	<div  class='col-md-8'> 
		<div class='altmetric-embed' data-badge-type='donut' 
		data-badge-details='right' data-doi='10.1140/epjc/s10052-012-2263-z'></div>
	</div>
</div>
- - - 
<div class="row">
	<div  class="col-md-4">
		Search for pair production of massive particles decaying into three quarks with the ATLAS detector in $\sqrt{s}=7$ TeV $pp$ collisions at the LHC
	</div>
	<div  class='col-md-8'> 
		<div class='altmetric-embed' data-badge-type='donut' 
		data-badge-details='right' data-doi='10.1007/JHEP12(2012)086'></div>
	</div>
</div>
- - - 
<div class="row">
	<div  class="col-md-4">
		Search for anomalous production of prompt like-sign lepton pairs at $\sqrt{s}=7$ TeV with the ATLAS detector
	</div>
	<div  class='col-md-8'> 
		<div class='altmetric-embed' data-badge-type='donut' 
		data-badge-details='right' data-doi='10.1007/JHEP12(2012)007'></div>
	</div>
</div>
- - - 
<div class="row">
	<div  class="col-md-4">
		Search for dark matter candidates and large extra dimensions in events with a jet and missing transverse momentum with the ATLAS detector
	</div>
	<div  class='col-md-8'> 
		<div class='altmetric-embed' data-badge-type='donut' 
		data-badge-details='right' data-doi='10.1007/JHEP04(2013)075'></div>
	</div>
</div>
- - - 
<div class="row">
	<div  class="col-md-4">
		Search for R-parity-violating supersymmetry in events with four or more leptons in $\sqrt{s}=7$ TeV $pp$ collisions with the ATLAS detector
	</div>
	<div  class='col-md-8'> 
		<div class='altmetric-embed' data-badge-type='donut' 
		data-badge-details='right' data-doi='10.1007/JHEP12(2012)124'></div>
	</div>
</div>
- - - 
<div class="row">
	<div  class="col-md-4">
		Measurement of $W^+W^-$ production in pp collisions at $\sqrt{s}$=7  TeV with the ATLAS detector and limits on anomalous WWZ and WWγ couplings
	</div>
	<div  class='col-md-8'> 
		<div class='altmetric-embed' data-badge-type='donut' 
		data-badge-details='right' data-doi='10.1103/PhysRevD.87.112001'></div>
	</div>
</div>
- - - 
<div class="row">
	<div  class="col-md-4">
		Search for direct chargino production in anomaly-mediated supersymmetry breaking models based on a disappearing-track signature in $pp$ collisions at $\sqrt{s}=7$ TeV with the ATLAS detector
	</div>
	<div  class='col-md-8'> 
		<div class='altmetric-embed' data-badge-type='donut' 
		data-badge-details='right' data-doi='10.1007/JHEP01(2013)131'></div>
	</div>
</div>
- - - 
<div class="row">
	<div  class="col-md-4">
		ATLAS search for new phenomena in dijet mass and angular distributions using $pp$ collisions at $\sqrt{s}=7$ TeV
	</div>
	<div  class='col-md-8'> 
		<div class='altmetric-embed' data-badge-type='donut' 
		data-badge-details='right' data-doi='10.1007/JHEP01(2013)029'></div>
	</div>
</div>
- - - 
<div class="row">
	<div  class="col-md-4">
		Search for Supersymmetry in Events with Large Missing Transverse Momentum, Jets, and at Least One Tau Lepton in 7 TeV Proton-Proton Collision Data with the ATLAS Detector
	</div>
	<div  class='col-md-8'> 
		<div class='altmetric-embed' data-badge-type='donut' 
		data-badge-details='right' data-doi='10.1140/epjc/s10052-012-2215-7'></div>
	</div>
</div>
- - - 
<div class="row">
	<div  class="col-md-4">
		Measurement of the flavour composition of dijet events in $pp$ collisions at $\sqrt{s}=7$ TeV with the ATLAS detector
	</div>
	<div  class='col-md-8'> 
		<div class='altmetric-embed' data-badge-type='donut' 
		data-badge-details='right' data-doi='10.1140/epjc/s10052-013-2301-5'></div>
	</div>
</div>
- - - 
<div class="row">
	<div  class="col-md-4">
		Search for displaced muonic lepton jets from light Higgs boson decay in proton-proton collisions at $\sqrt{s}=7$ TeV with the ATLAS detector
	</div>
	<div  class='col-md-8'> 
		<div class='altmetric-embed' data-badge-type='donut' 
		data-badge-details='right' data-doi='10.1016/j.physletb.2013.02.058'></div>
	</div>
</div>
- - - 
<div class="row">
	<div  class="col-md-4">
		Search for resonant top plus jet production in $t\bar{t}$ + jets events with the ATLAS detector in $pp$ collisions at $\sqrt{s}=7$ TeV
	</div>
	<div  class='col-md-8'> 
		<div class='altmetric-embed' data-badge-type='donut' 
		data-badge-details='right' data-doi='10.1103/PhysRevD.86.091103'></div>
	</div>
</div>
- - - 
<div class="row">
	<div  class="col-md-4">
		Search for dark matter candidates and large extra dimensions in events with a photon and missing transverse momentum in $pp$ collision data at $\sqrt{s}=7$ TeV with the ATLAS detector
	</div>
	<div  class='col-md-8'> 
		<div class='altmetric-embed' data-badge-type='donut' 
		data-badge-details='right' data-doi='10.1103/PhysRevLett.110.011802'></div>
	</div>
</div>
- - - 
<div class="row">
	<div  class="col-md-4">
		ATLAS search for a heavy gauge boson decaying to a charged lepton and a neutrino in $pp$ collisions at $\sqrt{s}=7$ TeV
	</div>
	<div  class='col-md-8'> 
		<div class='altmetric-embed' data-badge-type='donut' 
		data-badge-details='right' data-doi='10.1140/epjc/s10052-012-2241-5'></div>
	</div>
</div>
- - - 
<div class="row">
	<div  class="col-md-4">
		Search for a heavy top-quark partner in final states with two leptons with the ATLAS detector at the LHC
	</div>
	<div  class='col-md-8'> 
		<div class='altmetric-embed' data-badge-type='donut' 
		data-badge-details='right' data-doi='10.1007/JHEP11(2012)094'></div>
	</div>
</div>
- - - 
<div class="row">
	<div  class="col-md-4">
		Search for high-mass resonances decaying to dilepton final states in pp collisions at s**(1/2) = 7-TeV with the ATLAS detector
	</div>
	<div  class='col-md-8'> 
		<div class='altmetric-embed' data-badge-type='donut' 
		data-badge-details='right' data-doi='10.1007/JHEP11(2012)138'></div>
	</div>
</div>
- - - 
<div class="row">
	<div  class="col-md-4">
		Search for light top squark pair production in final states with leptons and $b^-$ jets with the ATLAS detector in $\sqrt{s}=7$ TeV proton-proton collisions
	</div>
	<div  class='col-md-8'> 
		<div class='altmetric-embed' data-badge-type='donut' 
		data-badge-details='right' data-doi='10.1016/j.physletb.2013.01.049'></div>
	</div>
</div>
- - - 
<div class="row">
	<div  class="col-md-4">
		Search for diphoton events with large missing transverse momentum in 7 TeV proton-proton collision data with the ATLAS detector
	</div>
	<div  class='col-md-8'> 
		<div class='altmetric-embed' data-badge-type='donut' 
		data-badge-details='right' data-doi='10.1016/j.physletb.2012.10.069'></div>
	</div>
</div>
- - - 
<div class="row">
	<div  class="col-md-4">
		Measurements of the pseudorapidity dependence of the total transverse energy in proton-proton collisions at $\sqrt{s}=7$ TeV with ATLAS
	</div>
	<div  class='col-md-8'> 
		<div class='altmetric-embed' data-badge-type='donut' 
		data-badge-details='right' data-doi='10.1007/JHEP11(2012)033'></div>
	</div>
</div>
- - - 
<div class="row">
	<div  class="col-md-4">
		Further search for supersymmetry at $\sqrt{s}=7$ TeV in final states with jets, missing transverse momentum and isolated leptons with the ATLAS detector
	</div>
	<div  class='col-md-8'> 
		<div class='altmetric-embed' data-badge-type='donut' 
		data-badge-details='right' data-doi='10.1103/PhysRevD.86.092002'></div>
	</div>
</div>
- - - 
<div class="row">
	<div  class="col-md-4">
		Search for light scalar top quark pair production in final states with two leptons with the ATLAS detector in $\sqrt{s}=7$ TeV proton-proton collisions
	</div>
	<div  class='col-md-8'> 
		<div class='altmetric-embed' data-badge-type='donut' 
		data-badge-details='right' data-doi='10.1140/epjc/s10052-012-2237-1'></div>
	</div>
</div>
- - - 
<div class="row">
	<div  class="col-md-4">
		Search for direct production of charginos and neutralinos in events with three leptons and missing transverse momentum in $\sqrt{s}=7$ TeV $pp$ collisions with the ATLAS detector
	</div>
	<div  class='col-md-8'> 
		<div class='altmetric-embed' data-badge-type='donut' 
		data-badge-details='right' data-doi='10.1016/j.physletb.2012.11.039'></div>
	</div>
</div>
- - - 
<div class="row">
	<div  class="col-md-4">
		Search for direct slepton and gaugino production in final states with two leptons and missing transverse momentum with the ATLAS detector in $pp$ collisions at $\sqrt{s}=7$ TeV
	</div>
	<div  class='col-md-8'> 
		<div class='altmetric-embed' data-badge-type='donut' 
		data-badge-details='right' data-doi='10.1016/j.physletb.2012.11.058'></div>
	</div>
</div>
- - - 
<div class="row">
	<div  class="col-md-4">
		Search for new phenomena in the $W W$ to $\ell \nu \ell$' $\nu$' final state in $pp$ collisions at $\sqrt{s}=7$ TeV with the ATLAS detector
	</div>
	<div  class='col-md-8'> 
		<div class='altmetric-embed' data-badge-type='donut' 
		data-badge-details='right' data-doi='10.1016/j.physletb.2012.11.040'></div>
	</div>
</div>
- - - 
<div class="row">
	<div  class="col-md-4">
		Search for direct top squark pair production in final states with one isolated lepton, jets, and missing transverse momentum in $\sqrt{s}=7$ TeV $pp$ collisions using 4.7 $fb^{-1}$ of ATLAS data
	</div>
	<div  class='col-md-8'> 
		<div class='altmetric-embed' data-badge-type='donut' 
		data-badge-details='right' data-doi='10.1103/PhysRevLett.109.211803'></div>
	</div>
</div>
- - - 
<div class="row">
	<div  class="col-md-4">
		Measurement of the jet radius and transverse momentum dependence of inclusive jet suppression in lead-lead collisions at $\sqrt{s_{NN}}$= 2.76 TeV with the ATLAS detector
	</div>
	<div  class='col-md-8'> 
		<div class='altmetric-embed' data-badge-type='donut' 
		data-badge-details='right' data-doi='10.1016/j.physletb.2013.01.024'></div>
	</div>
</div>
- - - 
<div class="row">
	<div  class="col-md-4">
		Search for a supersymmetric partner to the top quark in final states with jets and missing transverse momentum at $\sqrt{s}=7$ TeV with the ATLAS detector
	</div>
	<div  class='col-md-8'> 
		<div class='altmetric-embed' data-badge-type='donut' 
		data-badge-details='right' data-doi='10.1103/PhysRevLett.109.211802'></div>
	</div>
</div>
- - - 
<div class="row">
	<div  class="col-md-4">
		Measurement of $WZ$ production in proton-proton collisions at $\sqrt{s}=7$ TeV with the ATLAS detector
	</div>
	<div  class='col-md-8'> 
		<div class='altmetric-embed' data-badge-type='donut' 
		data-badge-details='right' data-doi='10.1140/epjc/s10052-012-2173-0'></div>
	</div>
</div>
- - - 
<div class="row">
	<div  class="col-md-4">
		Search for squarks and gluinos with the ATLAS detector in final states with jets and missing transverse momentum using 4.7 fb$^{-1}$ of $\sqrt{s}=7$ TeV proton-proton collision data
	</div>
	<div  class='col-md-8'> 
		<div class='altmetric-embed' data-badge-type='donut' 
		data-badge-details='right' data-doi='10.1103/PhysRevD.87.012008'></div>
	</div>
</div>
- - - 
<div class="row">
	<div  class="col-md-4">
		Time-dependent angular analysis of the decay $B_{s}^{0} \to J/{\psi\phi}$ and extraction of $\Delta\Gamma_{s}$ and the CP-violating weak phase $\phi_s$ by ATLAS
	</div>
	<div  class='col-md-8'> 
		<div class='altmetric-embed' data-badge-type='donut' 
		data-badge-details='right' data-doi='10.1007/JHEP12(2012)072'></div>
	</div>
</div>
- - - 
<div class="row">
	<div  class="col-md-4">
		Underlying event characteristics and their dependence on jet size of charged-particle jet events in $pp$ collisions at $\sqrt{s}=7$ TeV with the ATLAS detector
	</div>
	<div  class='col-md-8'> 
		<div class='altmetric-embed' data-badge-type='donut' 
		data-badge-details='right' data-doi='10.1103/PhysRevD.86.072004'></div>
	</div>
</div>
- - - 
<div class="row">
	<div  class="col-md-4">
		Observation of a new particle in the search for the Standard Model Higgs boson with the ATLAS detector at the LHC
	</div>
	<div  class='col-md-8'> 
		<div class='altmetric-embed' data-badge-type='donut' 
		data-badge-details='right' data-doi='10.1016/j.physletb.2012.08.020'></div>
	</div>
</div>
- - - 
<div class="row">
	<div  class="col-md-4">
		Measurement of charged-particle event shape variables in $\sqrt{s}=7$ TeV proton-proton interactions with the ATLAS detector
	</div>
	<div  class='col-md-8'> 
		<div class='altmetric-embed' data-badge-type='donut' 
		data-badge-details='right' data-doi='10.1103/PhysRevD.88.032004'></div>
	</div>
</div>
- - - 
<div class="row">
	<div  class="col-md-4">
		Search for magnetic monopoles in $\sqrt{s}=7$ TeV $pp$ collisions with the ATLAS detector
	</div>
	<div  class='col-md-8'> 
		<div class='altmetric-embed' data-badge-type='donut' 
		data-badge-details='right' data-doi='10.1103/PhysRevLett.109.261803'></div>
	</div>
</div>
- - - 
<div class="row">
	<div  class="col-md-4">
		Measurements of top quark pair relative differential cross-sections with ATLAS in $pp$ collisions at $\sqrt{s}=7$ TeV
	</div>
	<div  class='col-md-8'> 
		<div class='altmetric-embed' data-badge-type='donut' 
		data-badge-details='right' data-doi='10.1140/epjc/s10052-012-2261-1'></div>
	</div>
</div>
- - - 
<div class="row">
	<div  class="col-md-4">
		Search for top and bottom squarks from gluino pair production in final states with missing transverse energy and at least three b-jets with the ATLAS detector
	</div>
	<div  class='col-md-8'> 
		<div class='altmetric-embed' data-badge-type='donut' 
		data-badge-details='right' data-doi='10.1140/epjc/s10052-012-2174-z'></div>
	</div>
</div>
- - - 
<div class="row">
	<div  class="col-md-4">
		A search for $t\bar{t}$ resonances in lepton+jets events with highly boosted top quarks collected in $pp$ collisions at $\sqrt{s} = 7$ TeV with the ATLAS detector
	</div>
	<div  class='col-md-8'> 
		<div class='altmetric-embed' data-badge-type='donut' 
		data-badge-details='right' data-doi='10.1007/JHEP09(2012)041'></div>
	</div>
</div>
- - - 
<div class="row">
	<div  class="col-md-4">
		Measurement of the $\Lambda_b$ lifetime and mass in the ATLAS experiment
	</div>
	<div  class='col-md-8'> 
		<div class='altmetric-embed' data-badge-type='donut' 
		data-badge-details='right' data-doi='10.1103/PhysRevD.87.032002'></div>
	</div>
</div>
- - - 
<div class="row">
	<div  class="col-md-4">
		Combined search for the Standard Model Higgs boson in $pp$ collisions at $\sqrt{s} = 7$ TeV with the ATLAS detector
	</div>
	<div  class='col-md-8'> 
		<div class='altmetric-embed' data-badge-type='donut' 
		data-badge-details='right' data-doi='10.1103/PhysRevD.86.032003'></div>
	</div>
</div>
- - - 
<div class="row">
	<div  class="col-md-4">
		Search for the Standard Model Higgs boson produced in association with a vector boson and decaying to a $b$-quark pair with the ATLAS detector
	</div>
	<div  class='col-md-8'> 
		<div class='altmetric-embed' data-badge-type='donut' 
		data-badge-details='right' data-doi='10.1016/j.physletb.2012.10.061'></div>
	</div>
</div>
- - - 
<div class="row">
	<div  class="col-md-4">
		Search for the Higgs boson in the $H \to W W \to$ lnujj decay channel at $\sqrt{s}=7$ TeV with the ATLAS detector
	</div>
	<div  class='col-md-8'> 
		<div class='altmetric-embed' data-badge-type='donut' 
		data-badge-details='right' data-doi='10.1016/j.physletb.2012.10.066'></div>
	</div>
</div>
- - - 
<div class="row">
	<div  class="col-md-4">
		Search for the Standard Model Higgs boson in the $H$ to $\tau^{+} \tau^{-}$ decay mode in $\sqrt{s}=7$ TeV $pp$ collisions with ATLAS
	</div>
	<div  class='col-md-8'> 
		<div class='altmetric-embed' data-badge-type='donut' 
		data-badge-details='right' data-doi='10.1007/JHEP09(2012)070'></div>
	</div>
</div>
- - - 
<div class="row">
	<div  class="col-md-4">
		ATLAS measurements of the properties of jets for boosted particle searches
	</div>
	<div  class='col-md-8'> 
		<div class='altmetric-embed' data-badge-type='donut' 
		data-badge-details='right' data-doi='10.1103/PhysRevD.86.072006'></div>
	</div>
</div>
- - - 
<div class="row">
	<div  class="col-md-4">
		Measurement of the b-hadron production cross section using decays to $D^{*}\mu^-X$ final states in pp collisions at sqrt(s) = 7 TeV with the ATLAS detector
	</div>
	<div  class='col-md-8'> 
		<div class='altmetric-embed' data-badge-type='donut' 
		data-badge-details='right' data-doi='10.1016/j.nuclphysb.2012.07.009'></div>
	</div>
</div>
- - - 
<div class="row">
	<div  class="col-md-4">
		Search for a standard model Higgs boson in the mass range 200 - 600-GeV in the $H \to ZZ \to \ell^+ \ell^- q \bar{q}$ decay channel with the ATLAS detector
	</div>
	<div  class='col-md-8'> 
		<div class='altmetric-embed' data-badge-type='donut' 
		data-badge-details='right' data-doi='10.1016/j.physletb.2012.09.020'></div>
	</div>
</div>
- - - 
<div class="row">
	<div  class="col-md-4">
		Measurement of event shapes at large momentum transfer with the ATLAS detector in $pp$ collisions at $\sqrt{s}=7$ TeV
	</div>
	<div  class='col-md-8'> 
		<div class='altmetric-embed' data-badge-type='donut' 
		data-badge-details='right' data-doi='10.1140/epjc/s10052-012-2211-y'></div>
	</div>
</div>
- - - 
<div class="row">
	<div  class="col-md-4">
		Hunt for new phenomena using large jet multiplicities and missing transverse momentum with ATLAS in 4.7 fb$^{-1}$ of $\sqrt{s}=7$ TeV proton-proton collisions
	</div>
	<div  class='col-md-8'> 
		<div class='altmetric-embed' data-badge-type='donut' 
		data-badge-details='right' data-doi='10.1007/JHEP07(2012)167'></div>
	</div>
</div>
- - - 
<div class="row">
	<div  class="col-md-4">
		Search for the Standard Model Higgs boson in the $H \to$ WW(*) $\to \ell \nu \ell \nu$ decay mode with 4.7 /fb of ATLAS data at $\sqrt{s}=7$ TeV
	</div>
	<div  class='col-md-8'> 
		<div class='altmetric-embed' data-badge-type='donut' 
		data-badge-details='right' data-doi='10.1016/j.physletb.2012.08.010'></div>
	</div>
</div>
- - - 
<div class="row">
	<div  class="col-md-4">
		A search for flavour changing neutral currents in top-quark decays in $pp$ collision data collected with the ATLAS detector at $\sqrt{s}=7$ TeV
	</div>
	<div  class='col-md-8'> 
		<div class='altmetric-embed' data-badge-type='donut' 
		data-badge-details='right' data-doi='10.1007/JHEP09(2012)139'></div>
	</div>
</div>
- - - 
<div class="row">
	<div  class="col-md-4">
		Search for a Standard Model Higgs boson in the H -> ZZ -> $l^+l^-\nu \bar{\nu}$ decay channel using 4.7 $fb^{-1}$ of sqrt(s) = 7 TeV data with the ATLAS detector
	</div>
	<div  class='col-md-8'> 
		<div class='altmetric-embed' data-badge-type='donut' 
		data-badge-details='right' data-doi='10.1016/j.physletb.2012.09.016'></div>
	</div>
</div>
- - - 
<div class="row">
	<div  class="col-md-4">
		Evidence for the associated production of a $W$ boson and a top quark in ATLAS at $\sqrt{s}=7$ TeV
	</div>
	<div  class='col-md-8'> 
		<div class='altmetric-embed' data-badge-type='donut' 
		data-badge-details='right' data-doi='10.1016/j.physletb.2012.08.011'></div>
	</div>
</div>
- - - 
<div class="row">
	<div  class="col-md-4">
		A search for $t\bar{t}$ resonances with the ATLAS detector in 2.05 fb$^{-1}$ of proton-proton collisions at $\sqrt{s}=7$ TeV
	</div>
	<div  class='col-md-8'> 
		<div class='altmetric-embed' data-badge-type='donut' 
		data-badge-details='right' data-doi='10.1140/epjc/s10052-012-2083-1'></div>
	</div>
</div>
- - - 
<div class="row">
	<div  class="col-md-4">
		Measurement of the $t$-channel single top-quark production cross section in $pp$ collisions at $\sqrt{s}=7$ TeV with the ATLAS detector
	</div>
	<div  class='col-md-8'> 
		<div class='altmetric-embed' data-badge-type='donut' 
		data-badge-details='right' data-doi='10.1016/j.physletb.2012.09.031'></div>
	</div>
</div>
- - - 
<div class="row">
	<div  class="col-md-4">
		Measurement of $W \gamma$ and $Z \gamma$ production cross sections in $pp$ collisions at $\sqrt{s}=7$ TeV and limits on anomalous triple gauge couplings with the ATLAS detector
	</div>
	<div  class='col-md-8'> 
		<div class='altmetric-embed' data-badge-type='donut' 
		data-badge-details='right' data-doi='10.1016/j.physletb.2012.09.017'></div>
	</div>
</div>
- - - 
<div class="row">
	<div  class="col-md-4">
		Measurement of the W boson polarization in top quark decays with the ATLAS detector
	</div>
	<div  class='col-md-8'> 
		<div class='altmetric-embed' data-badge-type='donut' 
		data-badge-details='right' data-doi='10.1007/JHEP06(2012)088'></div>
	</div>
</div>
- - - 
<div class="row">
	<div  class="col-md-4">
		Measurement of the top quark pair cross section with ATLAS in pp collisions at sqrt(s) = 7 TeV using final states with an electron or a muon and a hadronically decaying $\tau$ lepton
	</div>
	<div  class='col-md-8'> 
		<div class='altmetric-embed' data-badge-type='donut' 
		data-badge-details='right' data-doi='10.1016/j.physletb.2012.09.032'></div>
	</div>
</div>
- - - 
<div class="row">
	<div  class="col-md-4">
		Search for tb resonances in proton-proton collisions at $\sqrt{s}=7$ TeV with the ATLAS detector
	</div>
	<div  class='col-md-8'> 
		<div class='altmetric-embed' data-badge-type='donut' 
		data-badge-details='right' data-doi='10.1103/PhysRevLett.109.081801'></div>
	</div>
</div>
- - - 
<div class="row">
	<div  class="col-md-4">
		Search for lepton flavour violation in the emu continuum with the ATLAS detector in $\sqrt{s}=7$ TeV $pp$ collisions at the LHC
	</div>
	<div  class='col-md-8'> 
		<div class='altmetric-embed' data-badge-type='donut' 
		data-badge-details='right' data-doi='10.1140/epjc/s10052-012-2040-z'></div>
	</div>
</div>
- - - 
<div class="row">
	<div  class="col-md-4">
		Search for a fermiophobic Higgs boson in the diphoton decay channel with the ATLAS detector
	</div>
	<div  class='col-md-8'> 
		<div class='altmetric-embed' data-badge-type='donut' 
		data-badge-details='right' data-doi='10.1140/epjc/s10052-012-2157-0'></div>
	</div>
</div>
- - - 
<div class="row">
	<div  class="col-md-4">
		Search for scalar top quark pair production in natural gauge mediated supersymmetry models with the ATLAS detector in $pp$ collisions at $\sqrt{s}=7$ TeV
	</div>
	<div  class='col-md-8'> 
		<div class='altmetric-embed' data-badge-type='donut' 
		data-badge-details='right' data-doi='10.1016/j.physletb.2012.07.010'></div>
	</div>
</div>
- - - 
<div class="row">
	<div  class="col-md-4">
		Measurement of $\tau$ polarization in $W -> \tau \nu$ decays with the ATLAS detector in pp collisions at sqrt(s) = 7 TeV
	</div>
	<div  class='col-md-8'> 
		<div class='altmetric-embed' data-badge-type='donut' 
		data-badge-details='right' data-doi='10.1140/epjc/s10052-012-2062-6'></div>
	</div>
</div>
- - - 
<div class="row">
	<div  class="col-md-4">
		Search for supersymmetry in events with three leptons and missing transverse momentum in $\sqrt{s}=7$ TeV $pp$ collisions with the ATLAS detector
	</div>
	<div  class='col-md-8'> 
		<div class='altmetric-embed' data-badge-type='donut' 
		data-badge-details='right' data-doi='10.1103/PhysRevLett.108.261804'></div>
	</div>
</div>
- - - 
<div class="row">
	<div  class="col-md-4">
		Search for TeV-scale gravity signatures in final states with leptons and jets with the ATLAS detector at $\sqrt{s}=7$ TeV
	</div>
	<div  class='col-md-8'> 
		<div class='altmetric-embed' data-badge-type='donut' 
		data-badge-details='right' data-doi='10.1016/j.physletb.2012.08.009'></div>
	</div>
</div>
- - - 
<div class="row">
	<div  class="col-md-4">
		Search for supersymmetry with jets, missing transverse momentum and at least one hadronically decaying $\tau$ lepton in proton-proton collisions at $\sqrt{s}=7$ TeV with the ATLAS detector
	</div>
	<div  class='col-md-8'> 
		<div class='altmetric-embed' data-badge-type='donut' 
		data-badge-details='right' data-doi='10.1016/j.physletb.2012.06.061'></div>
	</div>
</div>
- - - 
<div class="row">
	<div  class="col-md-4">
		Search for charged Higgs bosons decaying via $H^{+} \to \tau \nu$ in top quark pair events using $pp$ collision data at $\sqrt{s}=7$ TeV with the ATLAS detector
	</div>
	<div  class='col-md-8'> 
		<div class='altmetric-embed' data-badge-type='donut' 
		data-badge-details='right' data-doi='10.1007/JHEP06(2012)039'></div>
	</div>
</div>
- - - 
<div class="row">
	<div  class="col-md-4">
		Search for resonant $WZ$ production in the $WZ \to \ell \nu \ell^\prime\ell^\prime$ channel in $\sqrt{s}=7$ TeV $pp$ collisions with the ATLAS detector
	</div>
	<div  class='col-md-8'> 
		<div class='altmetric-embed' data-badge-type='donut' 
		data-badge-details='right' data-doi='10.1103/PhysRevD.85.112012'></div>
	</div>
</div>
- - - 
<div class="row">
	<div  class="col-md-4">
		Search for pair production of a new quark that decays to a Z boson and a bottom quark with the ATLAS detector
	</div>
	<div  class='col-md-8'> 
		<div class='altmetric-embed' data-badge-type='donut' 
		data-badge-details='right' data-doi='10.1103/PhysRevLett.109.071801'></div>
	</div>
</div>
- - - 
<div class="row">
	<div  class="col-md-4">
		Search for the decay Bs0 -> mu mu with the ATLAS detector
	</div>
	<div  class='col-md-8'> 
		<div class='altmetric-embed' data-badge-type='donut' 
		data-badge-details='right' data-doi='10.1016/j.physletb.2012.06.013'></div>
	</div>
</div>
- - - 
<div class="row">
	<div  class="col-md-4">
		Search for events with large missing transverse momentum, jets, and at least two tau leptons in 7 TeV proton-proton collision data with the ATLAS detector
	</div>
	<div  class='col-md-8'> 
		<div class='altmetric-embed' data-badge-type='donut' 
		data-badge-details='right' data-doi='10.1016/j.physletb.2012.06.055'></div>
	</div>
</div>
- - - 
<div class="row">
	<div  class="col-md-4">
		Measurement of the $W W$ cross section in $\sqrt{s}=7$ TeV $pp$ collisions with the ATLAS detector and limits on anomalous gauge couplings
	</div>
	<div  class='col-md-8'> 
		<div class='altmetric-embed' data-badge-type='donut' 
		data-badge-details='right' data-doi='10.1016/j.physletb.2012.05.003'></div>
	</div>
</div>
- - - 
<div class="row">
	<div  class="col-md-4">
		Search for supersymmetry in $pp$ collisions at $\sqrt{s}=7$ TeV in final states with missing transverse momentum and $b^-$ jets with the ATLAS detector
	</div>
	<div  class='col-md-8'> 
		<div class='altmetric-embed' data-badge-type='donut' 
		data-badge-details='right' data-doi='10.1103/PhysRevD.85.112006'></div>
	</div>
</div>
- - - 
<div class="row">
	<div  class="col-md-4">
		Search for gluinos in events with two same-sign leptons, jets and missing transverse momentum with the ATLAS detector in $pp$ collisions at $\sqrt{s}=7$ TeV
	</div>
	<div  class='col-md-8'> 
		<div class='altmetric-embed' data-badge-type='donut' 
		data-badge-details='right' data-doi='10.1103/PhysRevLett.108.241802'></div>
	</div>
</div>
- - - 
<div class="row">
	<div  class="col-md-4">
		Measurement of the top quark mass with the template method in the $t \bar{t}$ -> lepton + jets channel using ATLAS data
	</div>
	<div  class='col-md-8'> 
		<div class='altmetric-embed' data-badge-type='donut' 
		data-badge-details='right' data-doi='10.1140/epjc/s10052-012-2046-6'></div>
	</div>
</div>
- - - 
<div class="row">
	<div  class="col-md-4">
		Search for heavy neutrinos and right-handed $W$ bosons in events with two leptons and jets in $pp$ collisions at $\sqrt{s}=7$ TeV with the ATLAS detector
	</div>
	<div  class='col-md-8'> 
		<div class='altmetric-embed' data-badge-type='donut' 
		data-badge-details='right' data-doi='10.1140/epjc/s10052-012-2056-4'></div>
	</div>
</div>
- - - 
<div class="row">
	<div  class="col-md-4">
		Measurement of $t \bar{t}$ production with a veto on additional central jet activity in pp collisions at sqrt(s) = 7 TeV using the ATLAS detector
	</div>
	<div  class='col-md-8'> 
		<div class='altmetric-embed' data-badge-type='donut' 
		data-badge-details='right' data-doi='10.1140/epjc/s10052-012-2043-9'></div>
	</div>
</div>
- - - 
<div class="row">
	<div  class="col-md-4">
		Jet mass and substructure of inclusive jets in $\sqrt{s}=7$ TeV $pp$ collisions with the ATLAS experiment
	</div>
	<div  class='col-md-8'> 
		<div class='altmetric-embed' data-badge-type='donut' 
		data-badge-details='right' data-doi='10.1007/JHEP05(2012)128'></div>
	</div>
</div>
- - - 
<div class="row">
	<div  class="col-md-4">
		Measurement of the charge asymmetry in top quark pair production in $pp$ collisions at $\sqrt{s}=7$ TeV using the ATLAS detector
	</div>
	<div  class='col-md-8'> 
		<div class='altmetric-embed' data-badge-type='donut' 
		data-badge-details='right' data-doi='10.1140/epjc/s10052-012-2039-5'></div>
	</div>
</div>
- - - 
<div class="row">
	<div  class="col-md-4">
		Observation of spin correlation in $t \bar{t}$ events from pp collisions at sqrt(s) = 7 TeV using the ATLAS detector
	</div>
	<div  class='col-md-8'> 
		<div class='altmetric-embed' data-badge-type='donut' 
		data-badge-details='right' data-doi='10.1103/PhysRevLett.108.212001'></div>
	</div>
</div>
- - - 
<div class="row">
	<div  class="col-md-4">
		Determination of the strange quark density of the proton from ATLAS measurements of the $W \to \ell \nu$ and $Z \to \ell\ell$ cross sections
	</div>
	<div  class='col-md-8'> 
		<div class='altmetric-embed' data-badge-type='donut' 
		data-badge-details='right' data-doi='10.1103/PhysRevLett.109.012001'></div>
	</div>
</div>
- - - 
<div class="row">
	<div  class="col-md-4">
		Measurement of inclusive two-particle angular correlations in pp collisions with the ATLAS detector at the LHC
	</div>
	<div  class='col-md-8'> 
		<div class='altmetric-embed' data-badge-type='donut' 
		data-badge-details='right' data-doi='10.1007/JHEP05(2012)157'></div>
	</div>
</div>
- - - 
<div class="row">
	<div  class="col-md-4">
		Search for second generation scalar leptoquarks in $pp$ collisions at $\sqrt{s}=7$ TeV with the ATLAS detector
	</div>
	<div  class='col-md-8'> 
		<div class='altmetric-embed' data-badge-type='donut' 
		data-badge-details='right' data-doi='10.1140/epjc/s10052-012-2151-6'></div>
	</div>
</div>
- - - 
<div class="row">
	<div  class="col-md-4">
		Measurement of the production cross section of an isolated photon associated with jets in proton-proton collisions at $\sqrt{s}=7$ TeV with the ATLAS detector
	</div>
	<div  class='col-md-8'> 
		<div class='altmetric-embed' data-badge-type='donut' 
		data-badge-details='right' data-doi='10.1103/PhysRevD.85.092014'></div>
	</div>
</div>
- - - 
<div class="row">
	<div  class="col-md-4">
		Forward-backward correlations and charged-particle azimuthal distributions in pp interactions using the ATLAS detector
	</div>
	<div  class='col-md-8'> 
		<div class='altmetric-embed' data-badge-type='donut' 
		data-badge-details='right' data-doi='10.1007/JHEP07(2012)019'></div>
	</div>
</div>
- - - 
<div class="row">
	<div  class="col-md-4">
		Measurement of the azimuthal anisotropy for charged particle production in $\sqrt{s_{NN}}=2.76$ TeV lead-lead collisions with the ATLAS detector
	</div>
	<div  class='col-md-8'> 
		<div class='altmetric-embed' data-badge-type='donut' 
		data-badge-details='right' data-doi='10.1103/PhysRevC.86.014907'></div>
	</div>
</div>
- - - 
<div class="row">
	<div  class="col-md-4">
		Searches for New Physics: Les Houches Recommendations for the Presentation of LHC Results
	</div>
	<div  class='col-md-8'> 
		<div class='altmetric-embed' data-badge-type='donut' 
		data-badge-details='right' data-doi='10.1140/epjc/s10052-012-1976-3'></div>
	</div>
</div>
- - - 
<div class="row">
	<div  class="col-md-4">
		Measurement of the polarisation of $W$ bosons produced with large transverse momentum in $pp$ collisions at $\sqrt{s}=7$ TeV with the ATLAS experiment
	</div>
	<div  class='col-md-8'> 
		<div class='altmetric-embed' data-badge-type='donut' 
		data-badge-details='right' data-doi='10.1140/epjc/s10052-012-2001-6'></div>
	</div>
</div>
- - - 
<div class="row">
	<div  class="col-md-4">
		Search for a light Higgs boson decaying to long-lived weakly-interacting particles in proton-proton collisions at $\sqrt{s}=7$ TeV with the ATLAS detector
	</div>
	<div  class='col-md-8'> 
		<div class='altmetric-embed' data-badge-type='donut' 
		data-badge-details='right' data-doi='10.1103/PhysRevLett.108.251801'></div>
	</div>
</div>