import ROOT, sys, os
from ROOT import *

path = "/afs/cern.ch/user/d/djamin/fcc_work/JetClustering/output/20180228_substructure_pt250_5000/"

mass  = ["1000","2000","5000","10000"]
proc  = ["qcd"  ,"wqq","zqq"   ]
color = [kBlue-4,kRed ,kGreen-3]
rec_gen = "reco"
var   = ["mass","massSD","tau1","tau2","tau3","tau21","tau32"]

for m in mass :
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

  h0.Scale(1./h0.Integral()); h0.Rebin(25); h0.SetLineWidth(5); h0.SetLineColor(color[0])
  h1.Scale(1./h1.Integral()); h1.Rebin(25); h1.SetLineWidth(5); h1.SetLineColor(color[1])
  h2.Scale(1./h2.Integral()); h2.Rebin(25); h2.SetLineWidth(5); h2.SetLineColor(color[2])

  c.cd(0)

  h0.SetTitle("")
  h0.GetXaxis().SetTitle(v)
  h0.GetYaxis().SetTitle("Normalized to 1.")

  h0.GetXaxis().SetTitleOffset(1.1)
  h0.GetYaxis().SetTitleOffset(1.5)

  h0max = h0.GetMaximum()
  h1max = h1.GetMaximum()
  h2max = h2.GetMaximum()
  hmax = h0max
  if hmax<h1max : hmax = h1max
  if hmax<h2max : hmax = h2max
  h0.SetMaximum(hmax*1.1)

  h0.Draw("hist")
  h1.Draw("hist same")
  h2.Draw("hist same")

  legend=TLegend(0.85,0.7,0.98,0.9)
  legend.AddEntry(h0, proc[0], "l")
  legend.AddEntry(h1, proc[1], "l")
  legend.AddEntry(h2, proc[2], "l")
  legend.Draw()

  c.Print('{}_{}_{}.png'.format(rec_gen,v, m))

