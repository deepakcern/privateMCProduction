echo "================= CMSRUN starting Step 1 ====================" >> job.log
cmsRun -j step2.log -p PSet.py
echo "================= CMSRUN finished Step 1 ====================" >> job.log
echo "================= CMSRUN starting Step 2 ====================" >> job.log
cmsRun -e -j step3.log step3_cfg.py
echo "================= CMSRUN finished Step 2 ====================" >> job.log

echo "================= CMSRUN starting Step 3 ====================" >> job.log
cmsRun -e -j FrameworkJobReport.xml step4_cfg.py
echo "================= CMSRUN finished Step 3 ====================" >> job.log

