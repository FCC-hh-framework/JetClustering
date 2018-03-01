import ROOT, sys, os
from ROOT import *

#path = "/afs/cern.ch/user/d/djamin/fcc_work/JetClustering/output/20180228_substructure_pt250_5000/"
path = sys.argv[1]

mass  = ["1000","2000","5000","10000"]
proc  = ["qcd"  ,"wqq","zqq"   ]
color = [kBlue-4,kRed ,kGreen-3]
rec_gen = "reco"
var     = ["mass"      ,"massSD"       ,"tau21"    ]
leg_var = ["mass [GeV]","SD mass [GeV]","#tau_{21}"]
#var     = ["mass","massSD","tau1","tau2","tau3","tau21","tau32"]

for m in mass :

 rebin=4
 if m=="2000"  : rebin = 5
 if m=="5000"  : rebin = 10
 if m=="10000" : rebin = 10

 for v in var :
  fileName = path+proc[0]+m+".root"
  f0 = ROOT.TFile(fileName)
  h0 = f0.Get(rec_gen+"/"+rec_gen+"_"+v)
  fileName = path+proc[1]+m+".root"
  f1 = ROOT.TFile(fileName)
  h1 = f1.Get(rec_gen+"/"+rec_gen+"_"+v)
  fileName = path+proc[2]+m+".root"
  f2 = ROOT.TFile(fileName)
  h2 = f2.Get(rec_gen+"/"+rec_gen+"_"+v)

  c = ROOT.TCanvas("", "", 1000, 1000)
  ROOT.gROOT.SetBatch(True)
  ROOT.gStyle.SetOptStat(0)

  h0_int = h0.Integral()
  h1_int = h1.Integral()
  h2_int = h2.Integral()
  h0.Scale(1./h0_int); h0.Rebin(rebin); h0.SetLineWidth(7); h0.SetLineColor(color[0])
  h1.Scale(1./h1_int); h1.Rebin(rebin); h1.SetLineWidth(7); h1.SetLineColor(color[1])
  h2.Scale(1./h2_int); h2.Rebin(rebin); h2.SetLineWidth(7); h2.SetLineColor(color[2])

  c.cd(0)

  h0.SetTitle(m+" GeV")
  h0.GetXaxis().SetTitle(leg_var[var.index(v)])
  h0.GetYaxis().SetTitle("Normalized to 1.")

  h0.GetXaxis().SetTitleOffset(1.1)
  h0.GetYaxis().SetTitleOffset(1.5)

  hmax = h0.GetMaximum(); hbinmax = h0.GetMaximumBin()
  if hmax<h1.GetMaximum() : hmax = h1.GetMaximum(); hbinmax = h1.GetMaximumBin()
  if hmax<h2.GetMaximum() : hmax = h2.GetMaximum(); hbinmax = h2.GetMaximumBin() 
  h0.SetMaximum(hmax*1.1)

  h0.Draw("hist")
  h1.Draw("hist same")
  h2.Draw("hist same")

  leg_pos="R"
  if hbinmax>h0.GetNbinsX()*3./5. : leg_pos="L"
  if leg_pos=="L" : legend=TLegend(0.10,0.70,0.40,0.90)
  #if leg_pos=="C" : legend=TLegend(0.35,0.70,0.65,0.90)
  if leg_pos=="R" : legend=TLegend(0.60,0.70,0.90,0.90)
  legend.AddEntry(h0, proc[0]+" = "+str(h0_int)+" events", "l")
  legend.AddEntry(h1, proc[1]+" = "+str(h1_int)+" events", "l")
  legend.AddEntry(h2, proc[2]+" = "+str(h2_int)+" events", "l")
  legend.Draw()

  c.Print('{}_{}_{}.png'.format(rec_gen,v, m))

