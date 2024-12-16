from django.shortcuts import render,redirect
import pickle

# Create your views here.

def home(request):
    return render(request,'mystellar/home.html')

def model(request):
    if request.method=='GET':
        return render(request,'mystellar/model.html')
    if request.method=='POST':
        alpha=request.POST.get('alpha')
        delta=request.POST.get('delta')
        i=request.POST.get('i')
        z=request.POST.get('z')
        run_ID=request.POST.get('run_ID')
        redshift=request.POST.get('redshift')
        plate=request.POST.get('plate')
        fiber_ID=request.POST.get('fiber_ID')

        m=[alpha,delta,i,z,run_ID,redshift,plate,fiber_ID]
        for v in m:
            try:
                float(v)
            except ValueError:
                error1='Input should be a number.'
                return render(request,'mystellar/model.html',{'error1':error1})
        
        def validate(value,min,max):
            if not(min<=float(value)<=max):
                return False
            return True
        
        new_l=[]
        new_l.append(validate(alpha,0,360))
        new_l.append(validate(delta,-19,83))
        new_l.append(validate(i,9,32))
        new_l.append(validate(z,-9999,29))
        new_l.append(validate(run_ID,109,8162))
        new_l.append(validate(redshift,0,7))
        new_l.append(validate(plate,266,12547))
        new_l.append(validate(fiber_ID,1,1000))

        flag=True
        for k in new_l:
            if k==False:
                flag=False
                error2='Input is out of range.'
                return render(request,'mystellar/model.html',{'error2':error2})
            
        request.session['alpha']=alpha
        request.session['delta']=delta
        request.session['i']=i
        request.session['z']=z
        request.session['run_ID']=run_ID
        request.session['redshift']=redshift
        request.session['plate']=plate
        request.session['fiber_ID']=fiber_ID

        return redirect('result')
        
def result(request):
    with open('model.pkl','rb') as f:
        m=pickle.load(f)
    w=[]
    w.append(float(request.session['alpha']))
    w.append(float(request.session['delta']))
    w.append(float(request.session['i']))
    w.append(float(request.session['z']))
    w.append(float(request.session['run_ID']))
    w.append(float(request.session['redshift']))
    w.append(float(request.session['plate']))
    w.append(float(request.session['fiber_ID']))

    y=m['model'].predict(m['scaler'].transform([w]))
    if y[0]==0:
        prediction='GALAXY'
    elif y[0]==1:
        prediction='STAR'
    elif y[0]==2:
        prediction='QSO'

    return render(request,'mystellar/result.html',{'prediction':prediction})
